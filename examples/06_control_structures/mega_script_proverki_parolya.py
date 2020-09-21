
username = input('KAK BAC ZOBYT: ')

if len(username) == 0:
    print('ВЫ НЕ ВВЕЛИ ИМЯ')
else:
    password = input('/7PIDYMAITE /7APOL: ')
    if len(password) < 8:
        print('ПАРОЛЬ СЛИШКОМ КОРОТКИЙ') 
    elif username.upper() in password.upper():
        print('ПАРОЛЬ СОДЕРЖИТ ЛОГИН')
    else:
        print('Пароль для пользователя {} установлен'.format(username))

