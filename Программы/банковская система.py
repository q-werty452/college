

# 1. Хранение данных
users = {
    "Davlet": {"password": "1234", "balance": 5800.0},
    "Zahro": {"password": "qwerty", "balance": 200.0}
}


def register():
    print("\nРегистрация ")
    username = input("Введите логин: ")

    if username in users:
        print("Такой пользователь уже существует!")
        return

    password = input("Введите пароль: ")
    users[username] = {"password": password, "balance": 0.0}
    print(f"Пользователь {username} успешно зарегистрирован! Баланс: 0.0 сом")


def login():
    print("\nВход в систему")
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    if username in users and users[username]["password"] == password:
        print(f"Добро пожаловать, {username}!")
        user_menu(username)
    else:
        print("Неверный логин или пароль!")


def user_menu(username):
    while True:
        print(f"\nМеню {username}")
        print("1 — Проверить баланс")
        print("2 — Пополнить счёт")
        print("3 — Снять деньги")
        print("4 — Выйти из аккаунта")

        choice = input("Выберите действие: ")

        if choice == "1":
            print(f"Ваш баланс: {users[username]['balance']}₽")

        elif choice == "2":
            q = int(input("Введите сумму пополнения: "))
            if q > 0:
                users[username]['balance'] += q
                print(f"Счёт пополнен! Текущий баланс: {users[username]['balance']} сом.")
            else:
                print("Сумма должна быть положительной!")

        elif choice == "3":
            amount = int(input("Введите сумму для снятия: "))  
            if amount <= 0:
                print("Сумма должна быть положительной!")
            elif amount > users[username]['balance']:
                print("Недостаточно средств!")
            else:
                users[username]['balance'] -= amount
                print(f"Вы сняли {amount} сом. Остаток: {users[username]['balance']} сом.")

        elif choice == "4":
            print(f"До свидания, {username}!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")


def main_menu():

    while True:
        print("\nБАНКОВСКАЯ СИСТЕМА")
        print("1 — Войти")
        print("2 — Зарегистрироваться")
        print("3 — Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Ошибка ввода! Введите 1, 2 или 3.")


main_menu()