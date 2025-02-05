from tinydb import TinyDB, Query
import constants



def find_user(login, password):
    #если юзер найден -- вернуть словари по типу whoami и ads из constants.py
    #если юзер не найден -- вернуть два None
        db = TinyDB(constants.DB_PATH)
        user = Query()
        responce = db.search((user["Login"] == login ) & (user["Passwd"] == password))
        if ((len(responce) == 0) or (len(responce) > 1)):
            return None, None
        elif (len(responce) == 1):
            return responce[0], responce[0]["ads"]

def regist_user(user_info):
    #Добавить пользователя в базу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    db = TinyDB(constants.DB_PATH)
    db.insert(user_info)
    return 0
def unregist_user(user_info):
    #Удалить пользователя из базы
    # вернуть 0 если операция успешна, 1 -- в противном случае
    db = TinyDB(constants.DB_PATH)
    user = Query()
    req = db.search((user["Login"] == user_info["Login"]) & (user["Passwd"] == user_info["Passwd"]))
    db.remove(req)
    return 0
def add_ads_for_user(login, password, ads):
    # добавить конкретному юзеру новую рекламу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    db = TinyDB(constants.DB_PATH)
    user = Query()
    responce = db.search((user["Login"] == login) & (user["Passwd"] == password))
    if ((len(responce) == 0) or (len(responce) > 1)):
        return 1
    elif (len(responce) == 1):
        responce[0]["ads"] += [ads]
        db.update(responce[0], (user["Login"] == login) & (user["Passwd"] == password))
        return 0

def remove_add_for_user(login, password, id):
    # удалить у конкретного юзера конкретную рекламу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    db = TinyDB(constants.DB_PATH)
    user = Query()
    responce = db.search((user["Login"] == login) & (user["Passwd"] == password))
    if ((len(responce) == 0) or (len(responce) > 1)):
        return 1
    elif (len(responce) == 1):
        rIndex = -1
        for i, add in enumerate(responce[0]["ads"]):
            if add["id"] == id:
                rIndex = i
        responce[0]["ads"].pop(rIndex)
        db.update(responce[0], (user["Login"] == login) & (user["Passwd"] == password))
        return 0

def change_add_for_user(login, password, addNew):
    # изменить содержание рекламного элемента
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0

def find_all_ads_with_category(category):
    # вернуть всю рекламу от пользователей с заданной категорией должности
    # формат вывода или список словарей с ключами FIO, Tel (взять от юзера-обладателя-объявления), Title, Adres, About, или None
    return None