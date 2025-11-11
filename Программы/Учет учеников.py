import json
import os

#  1.Добавление ученика. Запрашивает имя, возраст, балл и любимый предмет.
# Проверяет: длину имени (не более 16 и не менее 3 символов);
# После добавления сразу сохраняет обновлённый словарь в students.txt.
# 2.Удаление ученика. Запрашивает имя и удаляет его, если найден.
# После удаления записывает изменения в students.txt
# 3.Просмотр всех учеников. Выводит всех учеников построчно:
# Имя: Aman / Возраст: 16 лет
# Балл: 4.8 / Любимый предмет: Математика
# Загружает данные из файла перед показом (если файл существует).
# 4.Изменение данных ученика. Запрашивает имя. Позволяет изменить:
# 1 — возраст
# 2 — балл
# 3 — любимый предмет
# После изменения данные сохраняются в students.txt
# 5.Выход из программы

def load_students():
    if os.path.exists('students.txt'):
        with open('students.txt', 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_students(students):
    with open('students.txt', 'w', encoding='utf-8') as file:
        json.dump(students, file, ensure_ascii=False, indent=2)

def add_student(students):
    while True:
        name = input("Введите имя ученика: ")
        if 3 <= len(name) <= 16:
            break
        print("Имя должно быть от 3 до 16 символов")
    
    age = int(input("Введите возраст: "))
    grade = float(input("Введите балл: "))
    subject = input("Введите любимый предмет: ")
    
    students[name] = {
        "age": age,
        "grade": grade,
        "subject": subject
    }
    save_students(students)
    print("Ученик успешно добавлен")

def remove_student(students):
    name = input("Введите имя ученика для удаления: ")
    if name in students:
        del students[name]
        save_students(students)
        print("Ученик удален")
    else:
        print("Ученик не найден")

def show_students(students):
    if not students:
        print("Список учеников пуст")
        return
    
    for name, info in students.items():
        print(f"Имя: {name} / Возраст: {info['age']} лет")
        print(f"Балл: {info['grade']} / Любимый предмет: {info['subject']}\n")

def modify_student(students):
    name = input("Введите имя ученика для изменения: ")
    if name not in students:
        print("Ученик не найден")
        return
    
    print("Что изменить?")
    print("1 - возраст")
    print("2 - балл")
    print("3 - любимый предмет")
    
    choice = input("Выберите опцию: ")
    
    if choice == "1":
        students[name]["age"] = int(input("Новый возраст: "))
    elif choice == "2":
        students[name]["grade"] = float(input("Новый балл: "))
    elif choice == "3":
        students[name]["subject"] = input("Новый любимый предмет: ")
    else:
        print("Неверный выбор")
        return
    
    save_students(students)
    print("Данные обновлены")

def main():
    students = load_students()
    
    while True:
        print("\n1. Добавить ученика")
        print("2. Удалить ученика")
        print("3. Показать всех учеников")
        print("4. Изменить данные ученика")
        print("5. Выход")
        
        choice = input("\nВыберите действие: ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            remove_student(students)
        elif choice == "3":
            show_students(students)
        elif choice == "4":
            modify_student(students)
        elif choice == "5":
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
