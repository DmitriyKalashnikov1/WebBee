import json
import constants


def find_user(login, password):
    #если юзер найден -- вернуть словари по типу whoami и ads из constants.py
    #если юзер не найден -- вернуть два None
    data = {}
    with open(constants.DB_PATH, 'r') as fp:
        data = json.load(fp)
    correctUsers = []
    for user in data:
        if user["Login"] == login:
            correctUsers.append(user)
    if len(correctUsers) == 0:
        return None, None
    else:
        if len(correctUsers) > 1:
            user = {}
            for i in range(len(correctUsers)):
                if correctUsers[i]["Passwd"] == password:
                    user = correctUsers[i]
        else:
            user = correctUsers[0]
        adds = user.pop("ads")
        return user, adds

def regist_user(user_info):
    #Добавить пользователя в базу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    sucsess = 0
    data = {}
    try:
        with open(constants.DB_PATH, 'r') as fp:
            data = json.load(fp)
        data += {user_info}
        with open(constants.DB_PATH, 'r') as fp:
            json.dump(data,fp)
    except:
        sucsess = 1
    return sucsess
def unregist_user(user_info):
    #Удалить пользователя из базы
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0
def add_ads_for_user(login, password, ads):
    # добавить конкретному юзеру новую рекламу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0

def remove_add_for_user(login, password, id):
    # удалить у конкретного юзера конкретную рекламу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0

def change_add_for_user(login, password, addNew):
    # изменить содержание рекламного элемента
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0

def find_all_ads_with_category(category):
    # вернуть всю рекламу от пользователей с заданной категорией должности
    # формат вывода или список словарей с ключами FIO, Tel (взять от юзера-обладателя-объявления), Title, Adres, About, или None
    return None