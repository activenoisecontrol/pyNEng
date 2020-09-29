# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('CAM_table.txt') as mac:
    line_mac = []
    vlan = input('Введите номер VLAN: ')
    for line in mac:
        if line.split('   ')[0].lstrip(' ').isdigit() and int(line.split('   ')[0]) == int(vlan):
            line = line.rstrip('\n').split('   ')
            line.pop(2)
            line[0] = line[0].lstrip(' ')
            print('   '.join(line))

