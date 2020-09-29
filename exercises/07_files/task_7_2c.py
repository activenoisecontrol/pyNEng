# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv
file1 = argv[1]
file2 = argv[2]
ignore = ["duplex", "alias", "Current configuration"]
with open(file1) as src, open(file2,'w') as dst:
    for line in src:
        if line.startswith(tuple(ignore)):
            continue
        elif line.startswith(' '+ignore[0]):
            continue
        else:
            dst.write(line)

