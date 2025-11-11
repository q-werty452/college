students = {
    "Иванов": {
        "Математика": [5, 4],
        "История": [3, 4]
    },
    "Петров": {
        "Физика": [4, 5],
        "Литература": [5]
    },
    "Сидоров": {
        "Биология": [4, 3],
        "Математика": [5]
    },
    "Ахмед": {
        "География": [5, 5],
        "История": [4]
    },
    "Смирнова": {
        "Русский язык": [5, 4, 5],
        "Литература": [4, 5]
    }
}

while True:
    print("\nМеню:\n1-Показать всех учеников\n2-Добавить ученика\n3-Добавить предмет ученику\n4-Добавить оценку по предмету ученика\n5-Показать все предметы и оценки ученика\n6-Посчитать среднюю оценку ученика\n7-Посчитать общую среднюю оценку по классу\n8-Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        for name in students:
            print(name)
    elif choice == "2":
        name = input("Введите имя ученика: ")
        if name in students:
            print("Ученик уже есть.")
        else:
            students[name] = {}
            print("Ученик добавлен.")
    elif choice == "3":
        name = input("Введите имя ученика: ")
        if name in students:
            subject = input("Введите название предмета: ")
            if subject in students[name]:
                print("Предмет уже есть.")
            else:
                students[name][subject] = []
                print("Предмет добавлен.")
        else:
            print("Такого ученика нет.")
    elif choice == "4":
        name = input("Введите имя ученика: ")
        if name in students:
            subject = input("Введите название предмета: ")
            if subject in students[name]:
                mark = input("Введите оценку: ")
                if mark.isdigit():
                    students[name][subject].append(int(mark))
                    print("Оценка добавлена.")
                else:
                    print("Некорректная оценка.")
            else:
                print("У ученика нет такого предмета.")
        else:
            print("Такого ученика нет.")
    elif choice == "5":
        name = input("Введите имя ученика: ")
        if name in students:
            for subject in students[name]:
                print(f"{subject}: {students[name][subject]}")
        else:
            print("Такого ученика нет.")
    elif choice == "6":
        name = input("Введите имя ученика: ")
        if name in students:
            total = 0
            count = 0
            for marks in students[name].values():
                total += sum(marks)
                count += len(marks)
            if count > 0:
                print("Средняя оценка:", total / count)
            else:
                print("Нет оценок.")
        else:
            print("Такого ученика нет.")
    elif choice == "7":
        total = 0
        count = 0
        for subjects in students.values():
            for marks in subjects.values():
                total += sum(marks)
                count += len(marks)
        if count > 0:
            print("Общая средняя оценка по классу:", total / count)
        else:
            print("Нет оценок в классе.")
    elif choice == "8":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор.") 


 