SERVER = 'mysql.joinserver.xyz'
DATABASE = 's410037_NKEiVT3'
USERNAME = 'u410037_k64ns7mW31'
PASSWORD = 'gZxp@ULU.7.s+UGxvbA8M@4D'


from connect_to_mysql import connect_to_mysql
import mysql.connector


cnx = mysql.connector.connect(user=USERNAME, 
                            password=PASSWORD, 
                            host=SERVER, 
                            database=DATABASE)
cursor = cnx.cursor()

# Запрос-регистрация.
def add_user(login, password):
    cnx = mysql.connector.connect(user=USERNAME, 
                            password=PASSWORD, 
                            host=SERVER, 
                            database=DATABASE)
    if cnx and cnx.is_connected():
        # Если коннект прошел успешно создаем курсор.
        cursor = cnx.cursor()
        # Проверка на существование аккаунта, зарегистрированного на эту почту.
        try:
            check_user = (login, )
            check_query = ("select exists (select 1 from usersly where email = %s);")
            cursor.execute(check_query, check_user)
            answer = cursor.fetchone()
            if answer[0] == 1:
                return 3
        except mysql.connector.Error as err:
            print(f"Ошибка: {err}.")
            return False
        query = ('INSERT INTO usersly' 
            '(email, password)' 
            'VALUES (%s, %s);')
        # Запрос на создание записи с данными пользователя.
        try:
            user = (login, password) 
            cursor.execute(query, user)
            cnx.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Ошибка: {err}.")
            return False


# Авторизация.
def pass_user(login, password):
    cnx = mysql.connector.connect(user=USERNAME, 
                            password=PASSWORD, 
                            host=SERVER, 
                            database=DATABASE)
    if cnx and cnx.is_connected(): 
        # Если коннект прошел успешно создаем курсор.
        cursor = cnx.cursor()
        query = ('''SELECT password FROM usersly WHERE email = %s;''')
        # Проверка на идентичность паролей.
        try:
            user = (login, )
            cursor.execute(query, user)
            usr_password = cursor.fetchone()
            if usr_password[0] == password:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Ошибка: {err}.")
            return False


cnx.commit()
cursor.close()
cnx.close()

