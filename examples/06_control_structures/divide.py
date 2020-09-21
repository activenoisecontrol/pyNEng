# -*- coding: utf-8 -*-
while True:
    try:
        a = input('Введите первое число: ')
        b = input('Введите второе число: ')
        result = int(a)/int(b)
    except ValueError:
        print('Пожалуйста, вводите только числа')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    else:
        print(result)
        break
'''
Example:

$ python divide.py
Введите первое число: 3
Введите второе число: 1
Результат:  3

$ python divide.py
Введите первое число: 5
Введите второе число: 0
Результат:  На ноль делить нельзя

$ python divide.py
Введите первое число: qewr
Введите второе число: 3
Результат:  Пожалуйста, вводите только числа
'''
