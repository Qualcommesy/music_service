SERVER = 'mysql.joinserver.xyz'
DATABASE = 's410037_NKEiVT3'
USERNAME = 'u410037_k64ns7mW31'
PASSWORD = 'gZxp@ULU.7.s+UGxvbA8M@4D'

import mysql.connector



cnx = mysql.connector.connect(user=USERNAME, password=PASSWORD,
                              host=SERVER,
                              database=DATABASE)
cursor = cnx.cursor()


# Этот запрос создает таблицы в базе даных.
query = ('''
CREATE TABLE IF NOT EXISTS usersly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE playlists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    file_path VARCHAR(500) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE playlist_tracks (
    playlist_id INT NOT NULL,
    track_id INT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (playlist_id, track_id),
    FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE,
    FOREIGN KEY (track_id) REFERENCES tracks(id) ON DELETE CASCADE
);
''')

cursor.execute(query)

cnx.commit()
cursor.close()
cnx.close()