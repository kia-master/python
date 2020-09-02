#!/usr/local/bin/python3

"""

a. Кроме имени устройства, запрашивается также параметр устройства
b. Также отображается список возможных параметров.
Список параметров надо получить из словаря, а не прописывать вручную.
c. при запросе параметра, которого нет в словаре устройства,
отображалось сообщение 'Такого параметра нет'.
Задание относится только к параметрам устройств, не к самим устройствам.
Если выбран существующий параметр,
вывести информацию о соответствующем параметре, указанного устройства.
d. при запросе параметра, пользователь мог вводить название параметра
в любом регистре

Ограничение: нельзя изменять словарь london_co.

"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

name = input('Введите имя устройства: ')
param = input('Введите имя параметра ({}): '.format(', '.join(london_co[name].keys()))).lower()

print(london_co[name].get(param, 'Такого параметра нет'))