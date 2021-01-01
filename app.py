from flask import Flask, request
import pprint
from flask_cors import CORS
import requests
import json

import db_sample as db

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    connection = db.connect_db()
    result = db.fetch_target_table(connection, "user")
    pprint.pprint(result)
    connection.commit()
    return result[0]

@app.route("/id_token", methods=["POST"])
def receive_id_token():
    res = request.data.decode("utf-8")
    json_data = json.loads(res)
    id_token = str(json_data["idToken"])
    return {"id_token": id_token}


@app.route("/user_info", methods=["POST"])
def fetch_user_info():
    # connection = db.connect_db()
    # result = db.fetch_user_info(connection, user_id)
    # pprint.pprint(result)
    # connection.commit()
    res = request.get_data()
    return res

if __name__ == "__main__":
    app.run(debug=True)


