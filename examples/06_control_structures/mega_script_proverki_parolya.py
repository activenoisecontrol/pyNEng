
username = input('KAK BAC ZOBYT: ')
password = input('/7PIDYMAITE /7APOL: ')

if len(username) == 0:
    print('ВЫ НЕ ВВЕЛИ ИМЯ')
else:
    if len(password) < 8:
        print('ПАРОЛЬ СЛИШКОМ КОРОТКИЙ') 
    elif username in password:
        print('ПАРОЛЬ СОДЕРЖИТ ЛОГИН')
    else:
        print('Пароль для пользователя {} установлен'.format(username))

