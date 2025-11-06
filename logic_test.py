from DBCommands import pass_user, add_user


login = "qualcommes122@gmail.com"
password = "123"


# Проверка вывода при регистрации пользователя.
if add_user(login, password) == True:
    print('Успешно зарегистрирован.')
elif add_user(login, password) == 3:
    print('На этой почте зарегистрирован аккаунт.')
elif add_user(login, password) == False:
    print('Произошла ошибка. ')

# Проверка вывода при авторизации пользователя.
if pass_user(login, password) == True:
    print('Успешно вошел.')
elif pass_user(login, password) == False:
    print('Произошла ошибка.')