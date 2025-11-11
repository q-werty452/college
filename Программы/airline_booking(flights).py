
# Написать функцию airline_booking(flights), которая:
#  1. Позволяет пользователю покупать билеты (ввод города).
#  2. Если города нет → «Такого направления нет».
#  3. Если мест нет → «Билеты закончились».
#  4. Если есть → спросить количество билетов.
#  • Если мест меньше → вывести «Недостаточно мест».
#  • Иначе оформить покупку (уменьшить количество мест, добавить в корзину, увеличить сумму).
#  5. Если сумма покупки превысила 20000 сом, дать скидку 20%.
#  6. В конце вывести:
#  • список купленных билетов (город + количество),
#  • общую стоимость (с учётом скидки),
#  • остаток мест по каждому направлению.

flights = {
    "Москва": {"цена": 8000, "места": 5},
    "Стамбул": {"цена": 12000, "места": 3},
    "Париж": {"цена": 15000, "места": 2},
    "Бишкек": {"цена": 5000, "места": 6}
}

def airline_booking(flights):
    basket = {}
    total = 0
    while True:
        city = input("Введите город (стоп - закончить): ").strip().title()
        if city.lower() == "стоп":
            break
        if city not in flights:
            print("Такого направления нет")
            continue
        if flights[city]["места"] == 0:
            print("Билеты закончились")
            continue
        try:
            count = int(input(f"Сколько билетов в {city}? "))
        except ValueError:
            print("Введите число")
            continue
        if count > flights[city]["места"]:
            print(f"Недостаточно мест. Доступно билетов: {flights[city]['места']}")
            continue
        flights[city]["места"] -= count
        basket[city] = basket.get(city, 0) + count
        total += flights[city]["цена"] * count

    discount = 0
    if total > 20000:
        discount = int(total * 0.2)
        total -= discount

    print("\nКупленные билеты:")
    for city, count in basket.items():
        print(f"{city}: {count} шт.")
    print(f"Общая стоимость: {total} сом (скидка: {discount} сом)")
    print("Остаток мест по направлениям:")
    for city, info in flights.items():
        print(f"{city}: {info['места']} мест")

airline_booking(flights)