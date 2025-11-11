# В кинотеатре показываются фильмы, у каждого фильма есть:
# название, цена билета, возрастное ограничение.
# Программа должна предоставлять меню:
usl = """
1. Показать список фильмов 
2. Купить билет на фильм 
3. Отменить билет по имени зрителя.
4. Показать все купленные билеты .
5. Посчитать общую выручку кинотеатра.
6. Выйти из программы."""
movies = {
"Интерстеллар": (300, 12),
"Начало": (250, 16),
"Матрица": (200, 16),
"Аватар": (350, 12),
}

tickets = {}

while True:
    print(usl)
    choice = input("Выберите действие: ")

    if choice == "1":
        print("Список фильмов:")
        for movi, price in movies.items():
            print(f"{movi}: {price[0]} руб., {price[1]}+")
    elif choice == "2":
        viewer = input("Имя зрителя: ")
        if viewer in tickets:
            print("Уже есть билет.")
        else:
            age = input("Возраст: ")
            if age.isdigit():
                age = int(age)
                print("Фильмы:")
                for name, (price, min_age) in movies.items():
                    print(f"{name}: {price} руб., {min_age}+")
                film = input("Название фильма: ")
                if film in movies:
                    price, min_age = movies[film]
                    if age >= min_age:
                        tickets[viewer] = (age, film, price)
                        print("Билет куплен.")
                    else:
                        print("Возрастное ограничение.")
                else:
                    print("Нет такого фильма.")
            else:
                print("Некорректный возраст.")
    elif choice == "3":
        viewer = input("Введите имя зрителя для отмены билета: ")
        if viewer in tickets:
            del tickets[viewer]
            print("Билет отменён.")
            print(tickets)
        else:
            print("У этого зрителя нет билета.")
    elif choice == "4":
        if not tickets:
            print("Нет купленных билетов.")
        else:
            print("Купленные билеты:")
            for viewer, (age, film, price) in tickets.items():
                print(f"{viewer}, {age} лет, фильм: {film}, цена: {price} руб.")
    elif choice == "5":
        total = sum(ticket[2] for ticket in tickets.values())
        print("Общая выручка кинотеатра:", total, "руб.")
    elif choice == "6":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор.")


            

