library= {
    "Война и мир": ["Л.Толстой","Доступно"]
}

while True:
        print("\nМеню:\n1-Показать все категории и книги\n2-Добавить книгу\n4-Найти книгу по названию\n5-Показать все книги автора\n6-Показать общее количество книг\n7-Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            for genre in library:
                print("Жанр: ",{genre})
                for title in library[genre]:
                    print(f"  {title} - {library[genre][title]}")
        elif choice == "2":
            genre = input("Введите жанр: ")
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            if genre not in library:
                library[genre] = {}
            if title in library[genre]:
                print("Книга уже есть в этой категории.")
            else:
                library[genre][title] = author
                print("Книга добавлена.")
                print(library)
        elif choice == "3":
            genre = input("Введите жанр: ")
            title = input("Введите название книги: ")
            if genre in library and title in library[genre]:
                del library[genre][title]
                print("Книга удалена.")
                if not library[genre]:
                    del library[genre]
            else:
                print("Такой книги нет.")
        
        elif choice == "4":
            title = input("Введите название книги: ")
            for genre in library:
                if title in library[genre]:
                    print(f"Автор: {library[genre][title]}, Категория: {genre}")
                    break
            else:
                print("Книга не найдена.")
        elif choice == "5":
            author = input("Введите автора: ")
            count = 0
            for genre in library:
                for title in library[genre]:
                    if library[genre][title] == author:
                        print(f"{title} ({genre})")
                        count = count + 1
            if count == 0:
                print("Книг этого автора нет.")
        elif choice == "6":
            total = 0
            for genre in library:
                total = total + len(library[genre])
            print(f"Всего книг: {total}")
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")



