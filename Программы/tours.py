# Туристическое агентство предлагает клиентам туры в разные страны.
# Каждый тур имеет:
#  • цену,
#  • минимальный возраст,
#  • длительность (в днях),
#  • количество доступных путёвок.

# Клиент может:
#  1. Просматривать доступные туры.
#  2. Выбирать один или несколько туров.
#  3. Добавлять дополнительные услуги (страховка, экскурсии, трансфер и т.п.).
#  4. Получать скидку, если общая сумма > 100 000 сом.
#  5. При бронировании проверяется:
#  • возраст клиента,
#  • наличие мест,
#  • корректность данных.

# В конце программа должна вывести:
#  • список заказанных туров,
#  • итоговую сумму (со скидкой, если она есть),
#  • оставшиеся туры и количество мест.


tours = {
    "Турция (Анталия)": {"цена": 40000, "дни": 7, "возраст": 12, "места": 5},
    "ОАЭ (Дубай)": {"цена": 60000, "дни": 5, "возраст": 18, "места": 3},
    "Таиланд (Пхукет)": {"цена": 75000, "дни": 10, "возраст": 16, "места": 4},
    "Кыргызстан (Иссык-Куль)": {"цена": 15000, "дни": 4, "возраст": 0, "места": 6}
}

services = {
    "Страховка": 2000,
    "Экскурсия": 3000,
    "Трансфер": 1500
}
def tour_booking(tours, services):
    basket = {}
    services_basket = {}
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            if age <= 0:
                print("Введите правильный возраст!")
                continue
            break
        except ValueError:
            print("Введите правильный возраст")

    total = 0
    while True:
        print("\nДоступные туры:")
        for name, info in tours.items():
            print(f"{name}: {info['цена']} сом, {info['дни']} дней, мин. возраст: {info['возраст']}, мест: {info['места']}")
        tour_name_input = input("Выберите тур (стоп - закончить): ").strip().lower()
        if tour_name_input == "стоп":
            break

        found_tour = None
        for name in tours:
            name_lower = name.lower()
            if tour_name_input in name_lower:
                found_tour = name
                break
            word = ""
            for ch in name_lower:
                if ch.isalnum():
                    word += ch
                else:
                    if word and tour_name_input == word:
                        found_tour = name
                        break
                    word = ""
            if not found_tour and word and tour_name_input == word:
                found_tour = name
            if found_tour:
                break

        if not found_tour:
            print("Такого тура нет")
            continue
        tour_name = found_tour
        tour = tours[tour_name]
        print(f"Вы выбрали '{tour_name}' за {tour['цена']} сом.")
        if age < tour["возраст"]:
            print("Вы не подходите по возрасту для этого тура.")
            continue
        if tour["места"] == 0:
            print("Мест нет.")
            continue
        try:
            count = int(input(f"Сколько путёвок в '{tour_name}'? "))
        except ValueError:
            print("Введите число.")
            continue
        if count < 1 or count > tour["места"]:
            print(f"Доступно только {tour['места']} мест.")
            continue
        tours[tour_name]["места"] -= count
        if tour_name in basket:
            basket[tour_name] += count
        else:
            basket[tour_name] = count
        total += tour["цена"] * count

        print("\nДополнительные услуги:")
        for s_name, s_price in services.items():
            print(f"{s_name}: {s_price} сом")
        add_service = input("Добавить услуги? (да/нет): ").strip().title()
        if add_service == "Да":
            for s_name in services:
                try:
                    s_count = int(input(f"{s_name} (сколько): "))
                except ValueError:
                    s_count = 0
                if s_count > 0:
                    if s_name in services_basket:
                        services_basket[s_name] += s_count
                    else:
                        services_basket[s_name] = s_count
                    total += services[s_name] * s_count

    discount = 0
    if total > 100000:
        discount = int(total * 0.1)
        total -= discount

    print("\nВаш заказ:")
    for name, count in basket.items():
        print(f"{name}: {count} шт.")
    for s_name, s_count in services_basket.items():
        print(f"{s_name}: {s_count} шт.")
    print(f"Итого к оплате: {total} сом (скидка: {discount} сом)")
    print("\nОставшиеся туры и количество мест:")
    for name, info in tours.items():
        print(f"{name}: {info['места']} мест")

tour_booking(tours, services)
