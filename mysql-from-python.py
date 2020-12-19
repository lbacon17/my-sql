import os
import datetime
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
        list_of_names = ['Jim', 'Bob', 'Fred']
        # prepare a string with the same number of placeholders 
        # as in list of names
        format_strings = ",".join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});"
                       .format(format_strings), list_of_names)
        connection.commit()
finally:
    # close connection, regardless of whether data pull successful or not
    connection.close()