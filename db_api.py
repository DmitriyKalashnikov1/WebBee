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