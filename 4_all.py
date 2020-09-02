# -*- coding: utf-8 -*-
###
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat.replace('FastEthernet', 'Gigabit')

###
mac = "AAAA:BBBB:CCCC"
mac.replace(':', '.')

###
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlan = config.split()
print(vlan)
vlans = vlan[-1].split(',')
print(vlans)

###
# уникальный список VLANов, отсортированный по возрастанию номеров
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
new_vlans = sorted(set(vlans))
print(new_vlans)

###
# Из строк command1 и command2 получить список VLANов,
# которые есть и в команде command1 и в команде command2 (пересечение).
# Результатом должен быть такой список: ['1', '3', '8']
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

v1 = command1.split()
v2 = command2.split()

vlan1 = set(v1[-1].split(','))
vlan2 = set(v2[-1].split(','))

vlans = vlan1.intersection(vlan2)

###
# Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
# Prefix                10.0.24.0/24
# AD/Metric             110/41
# Next-Hop              10.0.13.3
# Last update           3d18h
# Outbound Interface    FastEthernet0/0

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
string = ospf_route.split()

pref = string[0]
metr = string[1].strip('[]')
hop = string[3].rstrip(',')
upd = string[4].rstrip(',')
inter = string[5]

template = ('Prefix{:>28}\n'
            'AD/Metric{:>19}\n'
            'Next-Hop{:>23}\n'
            'Last update{:>16}\n'
            'Outbound Interface{:>19}')

ospf = template.format(pref, metr, hop, upd, inter)
print(ospf)

###
# Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
# '101010101010101010111011101110111100110011001100'

mac = "AAAA:BBBB:CCCC"
tmp = mac.split(':')

s1 = bin(int(tmp[0], 16))
s2 = bin(int(tmp[1], 16))
s3 = bin(int(tmp[2], 16))

mac_bin = (str(s1)+str(s2)+str(s3)).replace('0b', '')
print((str(s1)+str(s2)+str(s3)).replace('0b', ''))

###
# Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
# - первой строкой должны идти десятичные значения байтов
# - второй строкой двоичные значения
#
# Вывод должен быть упорядочен также, как в примере:
# - столбцами
# - ширина столбца 10 символов
#
# Пример вывода для адреса 10.1.1.1:
# 10        1         1         1
# 00001010  00000001  00000001  00000001

ip = "192.168.3.1"
tmp = ip.split('.')

ip_template = '''
     {0:<10} {1:<10} {2:<10} {3:<10}
     {0:010b} {1:010b} {2:010b} {3:010b}
      '''
print(ip_template.format(int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3])))


