import mysql.connector


def database_connector():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="kotsios",
        password="root",
        database="test",
        auth_plugin='mysql_native_password'
    )
    return mydb
