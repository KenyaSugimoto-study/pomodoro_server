from flask import Flask, request
import pprint
from flask_cors import CORS
import requests
import json

import db_sample as db
import firebase

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
    # POSTされたid_tokenをパース
    res = request.data.decode("utf-8")
    json_data = json.loads(res)
    # 各変数に代入
    id_token = str(json_data["idToken"])
    photoURL = str(json_data["photoURL"])
    family_name = str(json_data["familyName"])
    given_name = str(json_data["givenName"])
    is_new_user = json_data["isNewUser"]

    # id_tokenの検証
    uid = firebase.verify_id_token(id_token)

    # ユーザ名の結合
    user_name = family_name + " " + given_name

    connection = db.connect_db()
    # 新規ユーザであれば、DB追加の処理
    if is_new_user:
        new_user_info = {
            "uid": uid,
            "userName": user_name,
            "photoURL": photoURL,
        }
        db.add_new_user(connection, new_user_info)
        print("added new user")

        response_data = {
            "idToken": id_token,
            "uid": uid,
            "userName": user_name,
            "photoURL": photoURL,
            "totalWorkTime": 0
        }
    # 既存ユーザであれば、DB参照
    else:
        photoURL, total_work_time = db.fetch_user_info(connection, uid)
        response_data = {
            "idToken": id_token,
            "uid": uid,
            "userName": user_name,
            "photoURL": photoURL,
            "totalWorkTime": total_work_time
        }

    # フロント側にレスポンス
    return response_data


if __name__ == "__main__":
    app.run(debug=True)


