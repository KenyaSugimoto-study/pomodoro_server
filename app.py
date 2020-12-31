from flask import Flask
import pprint

import db_sample as db

app = Flask(__name__)

@app.route("/")
def hello_world():
    connection = db.connect_db()
    result = db.fetch_target_table(connection, "user")
    pprint.pprint(result)
    connection.commit()
    return result[0]

@app.route("/user_info", methods=["POST"])
def fetch_user_info(user_id):
    connection = db.connect_db()
    result = db.fetch_user_info(connection, user_id)
    pprint.pprint(result)
    connection.commit()
    return result[0]

if __name__ == "__main__":
    app.run(debug=True)


