# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP: ')
while True:
    octets = ip.split('.')
    if len(octets)==4 and (octets[0]+octets[1]+octets[2]+octets[3]).isdigit() and int(octets[0]) + int(octets[1]) + int(octets[2]) + int(octets[3])<=4*255:
        if int(octets[0]) in range(1,224):
            print('Типа адреса: unicast')
        elif int(octets[0]) in range(224,240):
            print('Типа адреса: multicast')
        elif ip == '255.255.255.255':
            print('Тип адреса: local broadcast')
        elif ip == '0.0.0.0':
            print('Тип адреса: unassigned')
        else:
            print('Тип адреса: unused')
        break
    else:
        ip = input('''IP-адрес введен некорректно.
Введите правильный IP-адрес: ''')
