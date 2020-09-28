# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt', 'r') as f:
    list_listov = []
    for line in f:
        list_listov.append(line.replace('O        ','').replace('via ','').replace(',','').rstrip().split(' '))
    for list in list_listov:
        print('''
Prefix               {}
AD/Metric            {}
Next-Hop             {}
Last Update          {}
Otbound Interface    {}
'''.format(list[0],list[1].strip('[]'),list[2],list[3],list[4]))


