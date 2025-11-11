# Написать функцию concert_booking(concerts, services), которая:
# 1. Спрашивает у пользователя имя и возраст.
# 2. Позволяет покупать билеты (пока не введёт стоп).
# 3. Проверяет: есть ли концерт в списке, хватает ли билетов, подходит ли возраст.
# 4. Если всё ок → спросить количество билетов.
# 5. После выбора концерта → спросить, нужны ли дополнительные услуги (несколько через запятую).
# • Стоимость каждой услуги × число билетов.
# 6. Сохранить заказ (концерт, билеты, услуги, цена).
# 7. Если сумма всех заказов > 50000 сом, то скидка 25%.
# 8. В конце вывести:
# • список всех заказов (с услугами), итоговую сумму (со скидкой или без), остаток билетов.
concerts = {
"Рок-фестиваль": {"цена": 4000, "билеты": 50, "возраст": 16},
"Джазовый вечер": {"цена": 3000, "билеты": 40, "возраст": 12},
"Классика в зале": {"цена": 2500, "билеты": 30, "возраст": 0},
"Поп-шоу": {"цена": 5000, "билеты": 20, "возраст": 10}
}

services = {
"VIP-место": 2000,
"Сувенир": 1000,
"Backstage-проход": 5000
}





def concert_booking(concerts, services):
    name = input("Введите ваше имя: ")
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            if age < 0:
                print("Ты дебил?")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число.")

    orders = []
    total_price = 0

    while True:
        print("\nДоступные концерты:")
        for c, info in concerts.items():
            print(f"{c} (Цена: {info['цена']} сом, Остаток билетов: {info['билеты']}, Возраст: {info['возраст']}+)")
        concert_name = input("Выберите концерт (или введите 'стоп' для завершения): ").strip()
        if concert_name.lower() == 'стоп':
            break

        if concert_name not in concerts:
            print("Такого концерта нет.")
            continue

        concert = concerts[concert_name]

        if concert["билеты"] <= 0:
            print("Билеты на этот концерт закончились.")
            continue

        if age < concert["возраст"]:
            print(f"Вам должно быть не менее {concert['возраст']} лет для этого концерта.")
            continue

        while True:
            try:
                num_tickets = int(input("Сколько билетов вы хотите купить? "))
                if num_tickets <= 0:
                    print("Количество билетов должно быть больше 0.")
                    continue
                if num_tickets > concert["билеты"]:
                    print(f"Доступно только {concert['билеты']} билетов.")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите число.")

        print("Доступные дополнительные услуги:", ', '.join(services.keys()))
        extras_input = input("Введите желаемые услуги через запятую (или оставьте пустым): ")
        selected_services = [s.strip() for s in extras_input.split(',') if s.strip() in services]

        base_cost = concert["цена"] * num_tickets
        services_cost = sum(services[s] * num_tickets for s in selected_services)
        order_cost = base_cost + services_cost
        total_price += order_cost

        orders.append({
            "концерт": concert_name,
            "билеты": num_tickets,
            "услуги": selected_services,
            "стоимость": order_cost
        })

        concert["билеты"] -= num_tickets
        print(f"Билеты на '{concert_name}' успешно куплены: {num_tickets} шт.")

    discount = 0
    if total_price > 50000:
        discount = int(total_price * 0.25)
        total_price -= discount

    print("\nКарзина:")
    for idx, order in enumerate(orders, 1):
        print(f"{idx}. Концерт: {order['концерт']}, Билетов: {order['билеты']}, "
              f"Услуги: {', '.join(order['услуги']) if order['услуги'] else 'Без доп. услуг'}, "
              f"Стоимость: {order['стоимость']} сом")

    print(f"\nСкидка: {discount} сом" if discount else "")
    print(f"Итоговая сумма: {total_price} сом")

    print("\nОстаток билетов по концертам:")
    for c, info in concerts.items():
        print(f"{c}: {info['билеты']} билетов осталось")


concerts = {
    "Рок-фестиваль": {"цена": 4000, "билеты": 50, "возраст": 16},
    "Джазовый вечер": {"цена": 3000, "билеты": 40, "возраст": 12},
    "Классика в зале": {"цена": 2500, "билеты": 30, "возраст": 0},
    "Поп-шоу": {"цена": 5000, "билеты": 20, "возраст": 10}
}

services = {
    "VIP-место": 2000,
    "Сувенир": 1000,
    "Backstage-проход": 5000
}

concert_booking(concerts, services)
