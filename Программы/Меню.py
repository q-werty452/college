menu_food = {
    1: ("Пицца", 350),
    2: ("Бургер", 250),
    3: ("Салат", 180),
    4: ("Суп", 150),
    5: ("Паста", 300),
    6: ("Стейк", 500),
    7: ("Рыба", 400),
    8: ("Картофель фри", 120),
    9: ("Шашлык", 350),
    10: ("Омлет", 130)
}

menu_drinks = {
    1: ("Чай", 50),
    2: ("Кофе", 80),
    3: ("Сок", 60),
    4: ("Вода", 40),
    5: ("Лимонад", 70),
    6: ("Молоко", 60),
    7: ("Квас", 55),
    8: ("Кока-кола", 75),
    9: ("Энергетик", 100),
    10: ("Компот", 65)
}
# basket = []
# priсе = []
# while True:
#     reg = input("Что вы хотите сделать?\n1 - Показать меню блюд\n2 - Показать меню напитков\n3 - Добавить блюдо в корзину\n4 - Добавить напиток в корзину\n5 - Показать корзину и итоговую сумму\n6 - Выйти\nВедите ваш выбор:")
#     if reg == "1":
#         print("Блюдо:")
#         for q,w in menu_food.items():
#             print(f"{q} {w}-сом")
#     elif reg == "2":
#         print("Напитки:")
#         for q,w in menu_drinks.items():
#             print(f"{q} {w}-сом")       
#     elif reg == "3":
#         print(menu_food)
#         chois = input("Ведите выбронное блюда:").title()
#         if chois in menu_food:
#             priсе.append(menu_food[chois])
#             basket.append(menu_food[chois])
#             print(f"{chois}-Добавлено в корзинку его цена {priсе}")
#             print (f"Итоговая цена:{basket} ")
#         else :
#             print("Нет такого блюда:)")
#     elif reg == "4":
#         print(menu_food)
#         chois = input("Ведите выбронный напиток:").title()
#         if chois in menu_food:
#             priсе.append(menu_drinks[chois])
#             basket.append(menu_drinks[chois])
#             print(f"{chois}-Добавлено в корзинку его цена {priсе}")
#             print (f"Итоговая цена:{basket} ")
#         else :
#             print("Нет такого блюда:)")
#     elif reg == "5":
#         if not basket:
#             print("Карзина пусто")
#         else :
#             print("В вашей карзине:",len(basket))
#             total = sum(basket)
#             print ("Общая сумма ",total)
#     elif reg == "6":
#         break

cart = [] # корзина куда падает стоимость блюд
while True:
    req = input(' 1. Показать меню блюд\n2. Показать меню напитков\n3. Заказать блюдо\n4. Заказать напиток\n5. Показать корзину и итоговую сумму\n6. Выйти\nВыберите: ')
    if req == '1':
        for k,v in menu_food.items():
            print(f"{k} {v}сом")
    elif req == '2':
        for k,v in menu_drinks.items():
            print(f"{k} {v}сом")
    elif req == '3':
        print(menu_food)
        name_food = input("Какое блюдо хотите? ").title()
        if name_food in menu_food:
            cart.append(menu_food[name_food])
            print(cart)
        else:
            print("нет такого блюда")
    elif req == '4':
        print(menu_drinks)
        name_drink = input("Какой напиток хотите? ").title()
        if name_drink in menu_drinks:
            cart.append(menu_drinks[name_drink])
            print(cart)
        else:
            print("нет такого напитка")
    elif req == '5':
        if not cart:
            print("Корзина пуста")
        else:
            print("В вашей корзине: ", len(cart))
            total = sum(cart) 
            print('Общая сумма:', total)
    elif req == '6':
        break


    