# В кафе есть список заказов клиентов.
#  Каждый заказ-  это название (блюд строка).
#  Нужно написать программу, которая:
orders = ["кофе","чай ","пирог","капучино","Салат","краб"]

print("""
1. Список заказов
2. Сколько заказов на определенную букву
3. Поиск заказа с определенным словом 
4. Добавить заказ""")

choice = input("Выберите действие: ")

while True:
    if choice == "1":
        print("Список заказов:")
        for order in orders:
            print(order)
        break
    if choice == "2":
        letter = input("Введите букву: ").lower()
        count = sum(1 for order in orders if order.lower().startswith(letter))
        print(f"Количество заказов на букву '{letter}': {count}")
        break
    elif choice == "3":
        word = input("Введите слово для поиска: ").lower()
        found_orders = [order for order in orders if word in order.lower()]
        if found_orders:
            print("Найденные заказы:")
            for order in found_orders:
                print(order)
        else:
            print("Заказы не найдены.")
        break
    elif choice == "4":
        new_order = input("Введите название нового заказа: ")
        if new_order.isalpha():
            orders.append(new_order)
            print(f"Заказ '{new_order}' добавлен.")
            print(orders)
        else:
            print("Введите толко буквы")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
        choice = input("Выберите действие: ")