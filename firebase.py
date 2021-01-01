import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os
import pprint

# 環境変数(GOOGLE_APPLICATION_CREDENTIALS)の設定
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/kenya/pomodoroapp-eb9ac-firebase-adminsdk-bb4xs-c524180ac7.json"

# サーバーに Firebase Admin SDK を追加する
# https://firebase.google.com/docs/admin/setup?hl=ja#python
cred = credentials.Certificate(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
default_app = firebase_admin.initialize_app(cred)
print(default_app.name)

def fetch_users():
    # # ユーザー管理
    # # https://firebase.google.com/docs/auth/admin/manage-users?hl=ja#python
    uid = "PE9Df4XCibQbKW7lQh81cbEERjB2"
    user = auth.get_user(uid)
    print('Successfully fetched user data: {0}'.format(user.uid))

    email = "kenyasugimoto.tech@gmail.com"
    user = auth.get_user_by_email(email)
    print('Successfully fetched user data: {0}'.format(user.uid))

    # Iterate through all users. This will still retrieve users in batches,
    # buffering no more than 1000 users in memory at a time.
    for user in auth.list_users().iterate_all():
        print('User: ' + user.uid)


def verify_id_token(id_token):
    # Firebase Admin SDK を使用して ID トークンを確認する
    # id_token comes from the client app
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    print("verify idToken")
    return uid
