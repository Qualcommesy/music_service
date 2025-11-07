SERVER = 'localhost'
DATABASE = 'music_service'
USERNAME = 'root'
PASSWORD = '#589TgF90!$sHA_209'

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
