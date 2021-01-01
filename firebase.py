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



# Firebase Admin SDK を使用して ID トークンを確認する
# https://firebase.google.com/docs/auth/admin/verify-id-tokens?hl=ja#verify_id_tokens_using_the_firebase_admin_sdk
# id_token comes from the client app (shown above)
# id_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjI2MTI5YmE1NDNjNTZlOWZiZDUzZGZkY2I3Nzg5ZjhiZjhmMWExYTEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMTA2NjQ1MzQ5OTA4OC1pZjd0Y2xxNDhkbmswZnA2YXFkYTZuMzBidG8yMG0ycC5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjEwNjY0NTM0OTkwODgtaWY3dGNscTQ4ZG5rMGZwNmFxZGE2bjMwYnRvMjBtMnAuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTM2NTI0MzE2NzI3MjU5OTA5MzAiLCJlbWFpbCI6InNrXzVfMjRAeWFob28uY28uanAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6InNEbEdFWmlhTGNlSXF4YjdqLThISFEiLCJpYXQiOjE2MDk0NTc1NTksImV4cCI6MTYwOTQ2MTE1OX0.sSFMJy4CbkV78y7pssdEgJgo1rUeWPxKwMXcCCB8RRhuKhVk5qcM2Y2tj9vj3fgfdClyDXvJxct6ewAh9PhvPcY_xH_QnXIiD-eqTPvDfX1fc7f6zYtYHmtKXXAXffrFrhnYbvWdCXz4g9umfHIFXLwuTxU66eJSxqEpmnv3nejAsyjKqWDOuD3gGAhIzvWskotIbRP9-LCnEgxQVr0k-KTE57YRO1wfIZIxbJREnZr4hqmtoWUzwHO10egahcrtn4LbhVYnbQiryFPijwMPBhzTqcndlraQX8NkMxK0jK-Xs_glqrzA5oRCEqkVx1OdAaCtIClib3ae09Z9uFX6og"
# decoded_token = auth.verify_id_token(id_token)
# # print(decoded_token)
# uid = decoded_token['uid']

# print(uid)
