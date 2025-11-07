SERVER = 'mysql.joinserver.xyz'
DATABASE = 's410037_NKEiVT3'
USERNAME = 'u410037_k64ns7mW31'
PASSWORD = 'gZxp@ULU.7.s+UGxvbA8M@4D'

import mysql.connector



cnx = mysql.connector.connect(user=USERNAME, password=PASSWORD,
                              host=SERVER,
                              database=DATABASE)
cursor = cnx.cursor()
# Этот запрос удаляет все таблицы базы данных. Создан для удобства разработки.
query = ('''
         DROP TABLE IF EXISTS playlist_tracks;
         DROP TABLE IF EXISTS tracks;
         DROP TABLE IF EXISTS playlists;
         DROP TABLE IF EXISTS usersly;
         ''')

cursor.execute(query)
cnx.commit()
cursor.close()
cnx.close()
