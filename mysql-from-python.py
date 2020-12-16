import os
import pymysql

# get username from workspace
username = os.getenv('USER_NAME')

# connect to database
connection = pymysql.connect(host='localhost', 
                             user=username, 
                             password='', 
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall
        print(result)
finally:
    # close connection, regardless of whether data pull successful or not
    connection.close()