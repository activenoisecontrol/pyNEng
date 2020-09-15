#from sys import argv

#interface, vlan = argv[1:3]

#print(argv)

interface = input('Введите тип и номер интерфейса: ')
vlan = input('Введите номер VLAN: ')

access_template = ['interface {}',
        'switchport mode access',
        'switchport access vlan {}',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable']

print('\n' + '=' * 30)
print('\n'.join(access_template).format(interface,vlan))

