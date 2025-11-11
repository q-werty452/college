# Написать функцию car_rental(cars, services), которая:
# 1. Спрашивает у пользователя имя и количество пассажиров.
# 2. Позволяет арендовать машину (пока не введёт стоп).
# 3. Проверяет: есть ли такая категория, есть ли свободные машины, хватает ли мест для пассажиров.
# 4. Если всё ок → спросить количество дней.
# 5. После выбора машины → спросить про дополнительные услуги (несколько через запятую).
# • Каждая услуга оплачивается за все дни аренды.
# 6. Сохранить заказ (машина, дни, услуги, цена).
# 7. Если сумма всех заказов > 25000 сом, то скидка 10%.
# 8. В конце вывести: список арендованных машин (с услугами), итоговую сумму, остаток машин по категориям.
cars = {
"Эконом": {"цена": 2000, "машины": 5, "макс_пассажиров": 4},
"Комфорт": {"цена": 3500, "машины": 3, "макс_пассажиров": 5},
"Бизнес": {"цена": 6000, "машины": 2, "макс_пассажиров": 5},
"Внедорожник": {"цена": 8000, "машины": 2, "макс_пассажиров": 7}
}
services = {
"Детское кресло": 500,
"GPS-навигация": 700,
"Страховка": 1500
}


def car_rental(cars, services):
    while True:
        name = input("Введите ваше имя: ")
        try:
            num_passengers = int(input("Сколько пассажиров поедет? "))
            if num_passengers <= 0:
                print("Количество пассажиров должно быть больше 0.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число.")

    orders = []
    total_price = 0

    while True:
        print("\nВыберите категорию машины:")
        print("Эконом")
        print("Комфорт")
        print("Бизнес")
        print("Внедорожник")
        category = input().strip().title()
        if category.lower() == 'стоп':
            break

        if category not in cars:
            print("Такой категории нет. Доступные категории:")
            print("Эконом")
            print("Комфорт")
            print("Бизнес")
            print("Внедорожник")
            continue

        car = cars[category]

        if car["машины"] <= 0:
            print("К сожалению, машин этой категории больше нет.")
            continue

        if num_passengers > car["макс_пассажиров"]:
            print(f"Эта машина вмещает только {car['макс_пассажиров']} пассажиров.")
            continue

        while True:
            try:
                days = int(input("На сколько дней вы хотите арендовать машину? "))
                if days <= 0:
                    print("Количество дней должно быть больше 0.")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите число.")

        print("Дополнительные услуги:")
        for s in services:
            print(s)
        selected_services = []
        while True:
            extras_input = input("Введите название услуги (или Enter если не нужны, 'стоп' для завершения): ").strip()
            if not extras_input or extras_input.lower() == 'стоп':
                break
            if extras_input in services:
                if extras_input not in selected_services:
                    selected_services.append(extras_input)
            else:
                print("Такой услуги нет. Доступные услуги:")
                for service in services:
                    print(service)

        base_cost = car["цена"] * days
        services_cost = 0
        for s in selected_services:
            services_cost += services[s] * days
        order_cost = base_cost + services_cost
        total_price += order_cost

        orders.append({
            "категория": category,
            "дней": days,
            "услуги": selected_services,
            "стоимость": order_cost
        })

        car["машины"] -= 1
        print(f"Машина категории '{category}' успешно арендована на {days} дней.")

    discount = 0
    if total_price > 25000:
        discount = int(total_price * 0.10)
        total_price -= discount

    print("\n--- Сводка заказов ---")
    for q, order in enumerate(orders, 1):
        print(f"{q}. Категория: {order['категория']}, Дней: {order['дней']}, ", end="")
        print("Услуги: ", end="")
        if order['услуги']:
            for i, s in enumerate(order['услуги']):
                if i > 0:
                    print(", ", end="")
                print(s, end="")
            print(f", Стоимость: {order['стоимость']} сом")
        else:
            print(f"Без доп. услуг, Стоимость: {order['стоимость']} сом")

    if discount:
        print(f"\nСкидка: {discount} сом")
    print(f"Итоговая сумма: {total_price} сом")

    print("\nОстаток машин по категориям:")
    for cat, info in cars.items():
        print(f"{cat}: {info['машины']} машин(ы) осталось")


car_rental(cars, services)