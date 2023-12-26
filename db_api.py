def find_user(login, password):
    #если юзер найден -- вернуть словари по типу whoami и ads из constants.py
    #если юзер не найден -- вернуть два None
    return None, None

def regist_user(user_info):
    #Добавить пользователя в базу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0
def unregist_user(user_info):
    #Удалить пользователя из базы
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0
def add_ads_for_user(login, password, ads):
    # добавить конкретному юзеру новую рекламу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0

def remove_ads_for_user(login, password, ads):
    # удалить у конкретного юзера конкретную рекламу
    # вернуть 0 если операция успешна, 1 -- в противном случае
    return 0