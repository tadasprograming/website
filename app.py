from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posted_data")
def post_data():
    return render_template("posted_data.html", data=request.args.get("data", "default_data"))

#if __name__ == "__main__":
    #app.run(debug=True)