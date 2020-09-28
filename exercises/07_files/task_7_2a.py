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
        elif line.startswith(' '+ignore[0]):
            continue
        else:
            print(line.rstrip())

