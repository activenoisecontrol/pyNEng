# -*- coding: utf-8 -*-

username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

while True:
    if len(password) < 8:
        print('Пароль слишком короткий')
    elif username in password:
        print('Пароль содержит имя пользователя')
    elif '@' not in password:
        print('В пароле должна быть @: ')
    else:
        print('Пароль для пользователя {} установлен'.format(username))
        break
    password = input('Введите пароль еще раз: ')
'''
Usage example:

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: nata1234
Пароль содержит имя пользователя

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 123nata123
Пароль содержит имя пользователя

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 1234
Пароль слишком короткий

$ python check_password.py
Введите имя пользователя: nata
Введите пароль: 123456789
Пароль для пользователя nata установлен
'''
