# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Enter network address: ').split('/')
address = ip[0].split('.')

mask = '1' * int(ip[1])
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

first = int(address[0])
second = int(address[1])
third = int(address[2])
fourth = int(address[3])

ip_bin = '{:08b}{:08b}{:08b}{:08b}'.format(first, second, third, fourth)
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
print('+'*50)
print('Вы ввели IP адрес ' + ip[0] + ' с префиксом ' + ip[1])

print(net_temp.format(oktet1, oktet2, oktet3, oktet4))

print(mask_temp.format(moktet1, moktet2, moktet3, moktet4))

