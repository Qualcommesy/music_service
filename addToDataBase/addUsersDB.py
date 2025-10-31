SERVER = 'mysql2.joinserver.xyz'
DATABASE = 's410037_NKEiVT2'
USERNAME = 'u410037_re3IqhHAoH'
PASSWORD = 'hnOw+LKzGcHrMtLt!QU5=A=w'

import mysql.connector



cnx = mysql.connector.connect(user=USERNAME, password=PASSWORD,
                              host=SERVER,
                              database=DATABASE)
cursor = cnx.cursor()

query = cnx.cursor()

query = ('''
CREATE TABLE IF NOT EXISTS Users(
id INT AUTO_INCREMENT PRIMARY KEY,
nickname VARCHAR(70) NOT NULL,
login VARCHAR(100) NOT NULL,
password NVARCHAR(100) NOT NULL),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
''')

cursor.execute(query)

cnx.commit()
cnx.close()