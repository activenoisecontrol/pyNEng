# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Enter network address: ').split('/')
address = ip[0].split('.')
first = int(address[0])
second = int(address[1])
third = int(address[2])
fourth = int(address[3])
net_temp = '''
    Network:
    {0:<8}  {1:<8}  {2:<8}  {3:<8}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''
print(net_temp.format(first, second, third, fourth))

mask = '1' * int(ip[1])
mask = '{:<032}'.format(mask)
moktet1 = int(mask[0:8],2)
moktet2 = int(mask[8:16],2)
moktet3 = int(mask[16:24],2)
moktet4 = int(mask[24:],2)
mask_temp = '''
    Mask:
    /{4:<}
    {0:<8}  {1:<8}  {2:<8}  {3:<8}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''
print(mask_temp.format(moktet1, moktet2, moktet3, moktet4, ip[1]))

