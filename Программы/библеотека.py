
library = {
    "Война и мир": ["Л.Толстой", "Доступно"],
    "Преступление и наказание": ["Ф.Достоевский", "Доступно"],
    "Мастер и Маргарита": ["М.Булгаков", "Доступно"],
    "Анна Каренина": ["Л.Толстой", "Доступно"],
    "Отцы и дети": ["И.Тургенев", "Доступно"],
    "Евгений Онегин": ["А.Пушкин", "Доступно"],
    "Доктор Живаго": ["Б.Пастернак", "Доступно"],
    "Обломов": ["И.Гончаров", "Доступно"],
    "Идиот": ["Ф.Достоевский", "Доступно"],
    "Дубровский": ["А.Пушкин", "Доступно"]
}

while True:
    print("\nМеню:\n1-Показать все книги\n2-Добавить книгу\n3-Удалить книгу\n4-Найти книгу по названию\n5-Показать все книги автора\n6-Взять книгу\n7-Вернуть книгу\n8-Общее количество книг\n9-Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        for title in library:
            print(f"{title} - Автор: {library[title][0]}, Статус: {library[title][1]}")
    elif choice == "2":
        title = input("Введите название книги: ")
        author = input("Введите автора: ")
        if title in library:
            print("Книга уже есть.")
        else:
            library[title] = [author, "Доступно"]
            print("Книга добавлена.")
    elif choice == "3":
        title = input("Введите название книги: ")
        if title in library:
            del library[title]
            print("Книга удалена.")
        else:
            print("Такой книги нет.")
    elif choice == "4":
        title = input("Введите название книги: ")
        if title in library:
            print(f"Автор: {library[title][0]}, Статус: {library[title][1]}")
        else:
            print("Книга не найдена.")
    elif choice == "5":
        author = input("Введите автора: ")
        count = 0
        for title in library:
            if library[title][0] == author:
                print(f"{title} - Статус: {library[title][1]}")
                count += 1
        if count == 0:
            print("Книг этого автора нет.")
    elif choice == "6":
        title = input("Введите название книги: ")
        if title in library:
            if library[title][1] == "Доступно":
                library[title][1] = "Выдано"
                print("Книга выдана.")
            else:
                print("Книга уже выдана.")
        else:
            print("Книга не найдена.")
    elif choice == "7":
        title = input("Введите название книги: ")
        if title in library:
            if library[title][1] == "Выдано":
                library[title][1] = "Доступно"
                print("Книга возвращена.")
            else:
                print("Книга уже доступна.")
        else:
            print("Книга не найдена.")
    elif choice == "8":
        print(f"Всего книг: {len(library)}")
    elif choice == "9":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор.")