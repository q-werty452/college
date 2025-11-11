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

basket = []

def show_menu(menu, title):
    print(f"\n{title}:")
    for num, (name, price) in menu.items():
        print(f"{num}. {name} - {price} руб.")

def show_basket():
    print("\nВаша корзина:")
    total = 0
    for item in basket:
        print(f"{item[0]} - {item[1]} руб.")
        total += item[1]
    print(f"Итого: {total} руб.")

while True:
    print("\nЧто вы хотите сделать?")
    print("1 - Показать меню блюд")
    print("2 - Показать меню напитков")
    print("3 - Добавить блюдо в корзину")
    print("4 - Добавить напиток в корзину")
    print("5 - Показать корзину и итоговую сумму")
    print("6 - Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        show_menu(menu_food, "Меню блюд")
    elif choice == "2":
        show_menu(menu_drinks, "Меню напитков")
    elif choice == "3":
        show_menu(menu_food, "Меню блюд")
        num = input("Введите номер блюда для добавления: ")
        if num.isdigit() and int(num) in menu_food:
            basket.append(menu_food[int(num)])
            print(f"{menu_food[int(num)][0]} добавлено в корзину.")
        else:
            print("Некорректный выбор.")
    elif choice == "4":
        show_menu(menu_drinks, "Меню напитков")
        num = input("Введите номер напитка для добавления: ")
        if num.isdigit() and int(num) in menu_drinks:
            basket.append(menu_drinks[int(num)])
            print(f"{menu_drinks[int(num)][0]} добавлено в корзину.")
        else:
            print("Некорректный выбор.")
    elif choice == "5":
        show_basket()
    elif choice == "6":
        print("Спасибо за заказ!")
        break
    else:
        print("Введите число от 1 до 6.")



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
            total = sum(cart) # считает все что в cart, прибавляет
            print('Общая сумма:', total)
    elif req == '6':
        break