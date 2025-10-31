SERVER = 'mysql2.joinserver.xyz'
DATABASE = 's410037_NKEiVT2'
USERNAME = 'u410037_re3IqhHAoH'
PASSWORD = 'hnOw+LKzGcHrMtLt!QU5=A=w'

import mysql.connector

cnx = mysql.connector.connect(user=USERNAME, password=PASSWORD,
                              host=SERVER,
                              database=DATABASE)

cursor = cnx.cursor()
query = (
'''
DROP TABLE Users
''')
cursor.execute(query)
cnx.commit()
cnx.close()