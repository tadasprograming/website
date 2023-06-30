from flask import Flask, render_template, request
from spreadsheet_evaluator_app import spreadsheet_evaluator
from cs50 import SQL
from scrape_app import scrape
from dice_app import dice_app

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
        
solved_functions_db = SQL("sqlite:///solved_functions.db")

@app.route("/post_data", methods=["GET", "POST"])
def post_data():
    if request.method == "GET":
        return render_template("post_data.html")
    elif request.method == "POST":
        data=request.form.get("data", "default_data")
        evaluated_data = spreadsheet_evaluator.solve_function(data)
        solved_functions_db.execute(
            "INSERT INTO solved_functions (Posted_function, Result) VALUES(?, ?)",
            data, evaluated_data
        )
        return render_template("posted.html", posted_data_placeholder=data,
                               evaluated_data_placeholder=evaluated_data)

@app.route("/posted_data", methods=["GET", "POST"])
def remove_data():
    if request.method == "GET":
        posted_data = solved_functions_db.execute(
            "SELECT * FROM solved_functions"
        )
        return render_template("posted_data.html", posted_data_placeholder=posted_data)
    elif request.method == "POST":
        line_to_remove_content = request.form.get("line_to_remove")
        if line_to_remove_content:
            solved_functions_db.execute(
            "DELETE FROM solved_functions WHERE Posted_function = ?", line_to_remove_content)
        posted_data = solved_functions_db.execute(
            "SELECT * FROM solved_functions"
        )
        return render_template("posted_data.html", posted_data_placeholder=posted_data)

@app.route("/scrape", methods=["GET", "POST"])
def scrape_page():
    if request.method == "GET":
        return render_template("scrape.html")
    if request.method == "POST":
        url = request.form.get("scrape_url")
        soup = scrape.scrape(url)
        scraped_info = scrape.find_info(soup)
        return render_template("scrape.html", scraped_info_placeholder=scraped_info,\
                                url_ph=url, soup_ph=soup)

game = dice_app.Game()
dice = dice_app.Dice()    
@app.route("/dice_game", methods=["GET", "POST"])
def dice_game_page():
    if request.method == "GET":
        return render_template("dice_game.html")
    if request.method == "POST":
        game_info = request.form.get("game_info")
        game.dice_amount, dice.sides, throws = map(int, game_info.split(', '))
        game.play(throws, dice.sides)
        results = game.throws_history
        results.reverse()        
        return render_template("dice_game.html", results_placeholder=results)


#if __name__ == "__main__":
    #app.run(debug=True)