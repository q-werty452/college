

contacts = {
    "Алексей": "79161234567",
    "Мария": "79261234568",
    "Иван": "79371234569",
    "Ольга": "79481234570",
    "Дмитрий": "79591234571",
    "Елена": "79601234572"
}

num_reg = input("Что вы хотите сделать?\n1-Добавить контакт\n2-Удалить контакт\n3-Поиск контакта\n4-Изменить контакт\n5-Показать все\nВыберите действие:")

if num_reg == "1":
    name = input("Введите имя: ")
    if len(name) > 2 and len(name) < 30:
        number = input("Введите номер: ")
        if len(number) == 9 and number.isdigit():
            contacts[name] = number
            print(f"Добавлен: {name} - {number}")
            print(contacts)
        else:
            print("Некорректный номер!")
    else:
        print("Некорректное имя!")
elif num_reg == "2":
    name = input("Введите имя для удаления: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} удалён.")
    else:
        print("Имя не найдено.")        
elif num_reg== "3":
        name = input("Введите имя для поиска: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Имя не найдено.")
elif num_reg == "4":
    for i in contacts.keys():
        print(i)
    choice = input("Что хотите изменить?\n1-Имя\n2-Номер\nВведите ваш выбор: ")
    if choice == "1":
        Old_name = input("Введите имя для изменения: ")
        if Old_name in contacts:
            new_name = input("Введите новое имя: ")
            contacts[new_name] = contacts.pop(Old_name)
            print(f"Имя для {Old_name} изменён на {new_name}")
            print(contacts)
        else:
            print("Имя не найдено.")
    elif choice == "2":
        name = input("Введите имя, чей номер хотите изменить: ")
        if name in contacts:
            new_number = input("Введите новый номер: ")
            contacts[name] = new_number
            print(f"Номер для {name} изменён на {new_number}")
            print(contacts)
        else:
            print("Имя не найдено.")
    else:
        print("Некорректный выбор.")
elif num_reg == "5":
        for name, number in contacts.items():
            print(f"{name}: {number}")
else:
    print("Введите 1, 2, 3, 4 или 5")

 






