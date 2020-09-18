# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ip = argv[1].split('/')
address = ip[0].split('.')
mask = ip[1]

mask = '1' * int(mask)
mask = '{:<032}'.format(mask)
moktet1 = int(mask[0:8],2)
moktet2 = int(mask[8:16],2)
moktet3 = int(mask[16:24],2)
moktet4 = int(mask[24:],2)
mask_temp = '''
    Mask:
    {0:<8}  {1:<8}  {2:<8}  {3:<8}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''

ip_bin = '{:08b}{:08b}{:08b}{:08b}'.format(int(address[0]),int(address[1]),int(address[2]),int(address[3]))
net_add = '{:>032}'.format(bin(int(ip_bin,2) & int(mask,2)).replace('0b',''))

oktet1 = int(net_add[0:8],2)
oktet2 = int(net_add[8:16],2)
oktet3 = int(net_add[16:24],2)
oktet4 = int(net_add[24:],2)
net_temp = '''
    Network:
    {0:<8}  {1:<8}  {2:<8}  {3:<8}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
print(' ')
print('+'*50)
print(' ')
print('Вы ввели IP адрес ' + ip[0] + ' с префиксом ' + ip[1])

print(net_temp.format(oktet1, oktet2, oktet3, oktet4))

print(mask_temp.format(moktet1, moktet2, moktet3, moktet4))


