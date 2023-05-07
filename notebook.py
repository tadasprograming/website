from cs50 import SQL

solved_functions_db = SQL("sqlite:///solved_functions.db")

posted_data = solved_functions_db.execute(
    "SELECT * FROM solved_functions"
)

print(posted_data)