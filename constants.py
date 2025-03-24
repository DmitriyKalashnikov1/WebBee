import os
import sys

AUTORS = [{"Name": "Калашников Дмитрий Александрович", "Work": "Главный разработчик данного сайта",
           "Email": "slagterra2017@yandex.ru", "Telephon": "8901235467"},
          {"Name": "Томаков Максим В.", "Work": "Гениральный директор сайта",
           "Email": "vasypupkin@yandex.ru", "Telephon": "85565342343"},
          #{"Name": "Поляков Матвей", "Work": "Специалист по БД",
          # "Email": "polykovMatvey@yandex.ru", "Telephon": "83458342343"}
          ]
WHOAMI = {
        "Login": "test_user",
        "Passwd": "2345671vx",
        "Name":"Иванов Владимир Т.",
        "Region": "Курская область, г.Курск",
        "Work":"Пчеловод",
        "Email": "vasypupkin@yandex.ru",
        "Telephon": "85565342343",
        "About": "Опытный пчеловод со стажем работы более 10-ти лет",
        "numberOfPassportofPasika": 5312420034569,
        "numberOfFamily": 50,
        "isStat": "Стационар",
        "hasMoveablePlatform": "Да",
        "purpose": "Медовое направление",
        "ads": []
}

Ads = [
    {
        "Title": "Липовый мед",
        "id": 1,
        "Adres": "Липовая улица 5, второй этаж, повильон 10",
        "About": "Продается липовый мед в 2х-литровых банках. Дата сбора:2003-07-04, Приходите, наш мед самый вкусный!"
    },
    {
        "Title": "Клиновый мед",
        "id": 2,
        "Adres": "Липовая улица 5, второй этаж, повильон 10",
        "About": "Продается клиновый мед в 3х-литровых банках. Дата сбора:2003-03-04, Приходите, наш мед самый вкусный!"
    }
]

DB_PATH = './DB.json'

HAS_TEST_DATA = False

def init():
    DB_PATH = os.path.join(sys._MEIPASS, "DB.json")