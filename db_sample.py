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

def add_new_user(connection, new_user_info):
    sql = "INSERT INTO user VALUES(NULL, %s, %s, %s, 0, 0);"
    with connection.cursor() as cursor:
        cursor.execute(sql, (new_user_info["uid"], new_user_info["userName"], new_user_info["photoURL"]))
        connection.commit()

def fetch_target_table(connection, target_table):
    with connection.cursor() as cursor:
        sql = f"select * from {target_table};"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

def fetch_user_info(connection, user_id):
    with connection.cursor() as cursor:
        sql = f"select * from user where userId = {user_id};"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

