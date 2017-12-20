from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='subx', 
                                 password='89731718',
                                 host='127.0.0.1',
                                 database='world')
cursor = cnx.cursor()
cursor.execute('select * from city where ID = 1')
values = cursor.fetchall()
print values
cursor.close()
cnx.close()