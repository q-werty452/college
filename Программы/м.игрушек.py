store = {
    "Мягкие игрушки": {"Мишка": 500, "Заяц": 400},
    "Конструкторы": {"Лего": 1200, "Магнитный конструктор": 950},
    "Куклы": {"Барби": 800, "Пупс": 600},
    "Машинки": {"Пожарная машина": 700, "Гоночная машина": 650}
}
cart = {}

while True:
    print("\n1. Показать все игрушки по категориям\n2. Добавить игрушку в корзину\n3. Удалить игрушку из корзины\n4. Показать корзину (все игрушки и итоговую сумму)\n5. Найти самую дорогую и самую дешёвую игрушку\n6. Показать количество игрушек в магазине\n7. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        for category in store:
            print(f"\n{category}:")
            for item in store[category]:
                print(f"  {item} - {store[category][item]} руб.")
    elif choice == "2":
        print("Доступные категории:")
        for category in store:
            print(category)
        cat = input("Введите категорию: ").title()
        if cat in store:
            print("Доступные игрушки:")
            for item in store[cat]:
                print(item)
            prod = input("Введите игрушку: ").title()
            if prod in store[cat]:
                cart[prod] = store[cat][prod]
                print(f"{prod} добавлена в корзину.")
                print(cart)
            else:
                print("Игрушка не найдена.")
        else:
            print("Категория не найдена.")
    elif choice == "3":
        if cart:
            print("Игрушки в корзине:")
            for item in cart:
                print(item)
            prod = input("Введите игрушку для удаления: ").title()
            if prod in cart:
                cart.pop(prod)
                print(f"{prod} удалена из корзины.")
            else:
                print("Игрушка не найдена в корзине.")
        else:
            print("Корзина пуста.")
    elif choice == "4":
        if cart:
            total = 0
            print("Корзина:")
            for item in cart:
                print(item, "-", cart[item], "руб.")
                total = total + cart[item]
            print("Итоговая сумма:", total, "руб.")
        else:
            print("Корзина пуста.")
    elif choice == "5":
        max_price = None
        min_price = None
        max_item = ""
        min_item = ""
        for category in store:
            for item in store[category]:
                price = store[category][item]
                if max_price is None or price > max_price:
                    max_price = price
                    max_item = item
                if min_price is None or price < min_price:
                    min_price = price
                    min_item = item
        if max_price is not None:
            print("Самая дорогая игрушка:", max_item, "-", max_price, "руб.")
            print("Самая дешёвая игрушка:", min_item, "-", min_price, "руб.")
        else:
            print("Нет игрушек в магазине.")
    elif choice == "6":
        count = 0
        for category in store:
            for item in store[category]:
                count = count + 1
        print("Количество игрушек в магазине:", count)
    elif choice == "7":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор.")