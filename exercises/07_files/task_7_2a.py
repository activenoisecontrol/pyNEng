# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
from sys import argv
file = argv[1]
print(file)
with open('config_sw1.txt') as f:
    for line in f:
        if line.startswith('!'):
            continue
        elif line.startswith(tuple(ignore)):
            continue
        else:
            print(line.rstrip())

