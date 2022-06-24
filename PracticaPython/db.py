import pymysql
from pymysql.cursors import DictCursor
import time


# Соединяемся с базой данных
dbh = pymysql.connect(
        host='db-learning.ithub.ru',
        user='2p2s17',
        password='484-906-465',
        db='2p2s17',
        charset='utf8mb4',
        cursorclass=DictCursor,
        autocommit=True
    )


def getDB():
    try:
        with dbh.cursor() as cur:
                sql = 'SELECT * FROM Notifications'
                cur.execute(sql)
                rows = cur.fetchall()
                return rows
    except:
        return {"Error": "error"}


def postDB_1():
    title = str(input("Input ur title: "))
    content = str(input("Input ur content: "))
    sql = f"INSERT Notifications(type, title, content, lastSentAt) VALUES ('SUCCES', '{title}', '{content}', UNIX_TIMESTAMP(NOW()))"
    return sql


def putDB(id):
    try:
        with dbh.cursor() as cur:
            title = str(input("Input ur title: "))
            content = str(input("Input ur content: "))
            sql = f"UPDATE Notifications SET id = id, type = type, title = '{title}', content = '{content}', lastSentAt = UNIX_TIMESTAMP(NOW()) WHERE id = {id};"
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
    except:
        return {"Error": "error"}


def deleteDB(id):
    try:
        with dbh.cursor() as cur:
            sql = f"DELETE FROM Notifications WHERE id = {id};"
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
    except:
        return {"Error": "error"}


def postDB_2(id):
    try:
        with dbh.cursor() as cur:
            sql = f"SELECT lastSentAt FROM Notifications"
            cur.execute(sql)
            rows = cur.fetchall()
            tim = rows[len(rows)-1]['lastSentAt']
            if len(str(tim)) > 5: 
                title = str(input("Input ur title: "))
                content = str(input("Input ur content: "))
                sql = f"INSERT Notifications(id, type, title, content, lastSentAt) VALUES ({id}, 'SUCCES', '{title}', '{content}', UNIX_TIMESTAMP(NOW())-{tim})"
                send_time = int(input("Через сколько минут отправить сообщение? "))
                time.sleep(60*send_time)
                cur.execute(sql)
                rows = cur.fetchall()
                return rows
            else:
                title = str(input("Input ur title: "))
                content = str(input("Input ur content: "))
                sql = f"INSERT Notifications(id, type, title, content, lastSentAt) VALUES ({id}, 'SUCCES', '{title}', '{content}', (UNIX_TIMESTAMP(NOW())+{tim} - UNIX_TIMESTAMP(NOW())))"
                send_time = int(input("Через сколько минут отправить сообщение? "))
                time.sleep(60*send_time)
                cur.execute(sql)
                rows = cur.fetchall()
                return rows
    except:
        return {"Error": "error"}
