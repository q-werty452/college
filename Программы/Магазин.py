# В магазине есть несколько категорий товаров:
# - Хлебобулочные
# - Мясо
# - Напитки
# Каждая категория хранится в словаре, где ключ — название товара, значение — цена.

# 1. Показать все товары по категориям.
# 2. Добавить товар в корзину.
# 3. Удалить товар из корзины.
# 4. Показать корзину (все товары и итоговую сумму).
# 5. Найти самый дорогой и самый дешёвый товар в магазине.
# 6. Показать количество товаров в магазине.
# 7. Выйти.

store = {
    "Хлебобулочные": {"Хлеб": 30, "Булочка": 20},
    "Мясо": {"Курица": 150, "Говядина": 700},
    "Напитки": {"Сок": 100, "Вода": 30}
}
cart = {}

while True:
    print("\n1. Показать все товары по категориям\n2. Добавить товар в корзину\n3. Удалить товар из корзины\n4. Показать корзину (все товары и итоговую сумму\n5. Найти самый дорогой и самый дешёвый товар в магазине\n6. Показать количество товаров в магазине\n7. Выйти")
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
            print("Доступные товары:")
            for item in store[cat]:
                print(item)
            prod = input("Введите товар: ").title()
            if prod in store[cat]:
                cart[prod] = store[cat][prod]
                print(f"{prod} добавлен в корзину.")
                print (cart)
            else:
                print("Товар не найден.")
        else:
            print("Категория не найдена.")
    elif choice == "3":
            if cart:
                print("Товары в корзине:")
                for item in cart:
                    print(item)
                prod = input("Введите товар для удаления: ")
                if prod in cart:
                    cart.pop(prod)
                    print(f"{prod} удалён из корзины.")
                else:
                    print("Товар не найден в корзине.")
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
            print("Самый дорогой товар:", max_item, "-", max_price, "руб.")
            print("Самый дешёвый товар:", min_item, "-", min_price, "руб.")
        else:
            print("Нет товаров в магазине.")
    elif choice == "6":
        count = 0
        for category in store:
            for item in store[category]:
                count = count + 1
        print("Количество товаров в магазине:", count)
    elif choice == "7":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор.")