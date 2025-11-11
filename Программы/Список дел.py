#  "список дел"
# Пользователь может :
# 1 Посмотреть список дел 
# 2 добавить новое дело
# 3 Удолить дело по названию 
# 4 отметить дело как выполненное 
# 5 Выйти 

todo = {}

while True:
    print("\n1. Посмотреть список дел\n2. Добавить новое дело\n3. Удалить дело по названию\n4. Отметить дело как выполненное\n5. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        if todo:
            print("\nСписок дел:")
            for name in todo:
                status = "Выполнено" if todo[name] else "Не выполнено"
                print(f"{name} - {status}")
        else:
            print("Список дел пуст.")
    elif choice == "2":
        name = input("Введите название дела: ")
        if name in todo:
            print("Такое дело уже есть.")
        else:
            todo[name] = "Не выполнено"
            print(f"Дело '{name}' добавлено. Статус: {todo[name]}")
    elif choice == "3":
        if todo:
            print("Дела:")
            for name in todo:
                print(name)
            name = input("Введите название дела для удаления: ")
            if name in todo:
                todo.pop(name)
                print(f"Дело '{name}' удалено.")
            else:
                print("Дело не найдено.")
        else:
            print("Список дел пуст.")
    elif choice == "4":
        if todo:
            print("Дела:")
            for name in todo:
                print(name)
            name = input("Введите название дела для отметки: ")
            if name in todo:
                todo[name] = True
                print(f"Дело '{name}' отмечено как выполненное.")
            else:
                print("Дело не найдено.")
        else:
            print("Список дел пуст.")
    elif choice == "5":
        print("Выход.")
        break
    else:
        print("Неверный выбор.")
        
                                                                                                                                                                                 