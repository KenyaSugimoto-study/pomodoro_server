import pymysql.cursors
from datetime import datetime
import pprint

def connect_db():
	connection = pymysql.connect(
		host="localhost",
		user="infolab",
		password="password",
		db="pomodoro",
		charset="utf8",
		cursorclass=pymysql.cursors.DictCursor
	)
	return connection

# 新しいユーザを登録
def add_new_user(connection, new_user_info):
    sql = "INSERT INTO user VALUES(NULL, %s, %s, %s, 0, 0);"
    with connection.cursor() as cursor:
        cursor.execute(sql, (new_user_info["uid"], new_user_info["userName"], new_user_info["photoURL"]))
        connection.commit()

# uidからDBのユーザ情報を取得
def fetch_user_info(connection, uid):
    try:
        with connection.cursor() as cursor:
            sql = "select * from user where uid = %s;"
            cursor.execute(sql, (uid))
            result = cursor.fetchall()

            response_data = result[0]

            return response_data
    except:
        return None

def update_total_work_time(connection, uid, total_work_time):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE user SET totalWorkTime=%s WHERE uid = %s;"
            cursor.execute(sql, (total_work_time, uid))
            connection.commit()

            return True
    except:
        return None
