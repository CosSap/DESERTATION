import mysql.connector


def database_connector(query):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="kotsios",
        password="root",
        database="test",
        auth_plugin='mysql_native_password'
    )

    cursor = mydb.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    mydb.close()

    return results


for row in database_connector(query="SELECT * FROM test_table"):
    print(row)

