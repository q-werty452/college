barbers = {
    "Алия": {"Стрижка": 500, "Бритьё": 300},
    "Давлет": {"Стрижка": 450, "Осветление": 800},
    "Ахмед": {"Модная стрижка": 700, "Укладка": 400}
}
 

record = []

while True:
    print("\nМеню:\n1 - Показать список барберов и их услуги\n2 - Записаться на услугу\n3 - Отменить запись по имени клиента\n4 - Показать все записи\n5 - Найти самого популярного барбера\n6 - Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        for barber, services in barbers.items():
            print(f"{barber}:")
            for service, price in services.items():
                print(f"  {service} - {price} руб.")
    elif choice == "2":
        name = input("Введите имя клиента: ")
        barber = input("Выберите барбера: ")
        if barber in barbers:
            print("Доступные услуги:")
            for service in barbers[barber]:
                print(service)
            service = input("Выберите услугу: ")
            if service in barbers[barber]:
                record.append({"client": name, "barber": barber, "service": service})
                print("Запись добавлена.")
            else:
                print("Нет такой услуги у выбранного барбера.")
        else:
            print("Нет такого барбера.")
    elif choice == "3":
            name = input("Введите имя клиента для отмены записи: ")
            before = len(record)
            record[:] = [app for app in record if app["client"] != name]
            if len(record) < before:
                print("Запись отменена.")
            else:
                print("Запись не найдена.")
    elif choice == "4":
            if record:
                for app in record:
                    print(f"{app['client']} записан к {app['barber']} на {app['service']}")
            else:
                print("Нет записей.")
    elif choice == "5":
            counts = {}
            for app in record:
                barber = app["barber"]
                counts[barber] = counts.get(barber, 0) + 1
            if counts:
                popular = max(counts, key=counts.get)
                print(f"Самый популярный барбер: {popular} ({counts[popular]} клиентов)")
            else:
                print("Нет записей.")
    elif choice == "6":
            print("Выход из программы.")
            break
    else:
            print("Некорректный выбор.")