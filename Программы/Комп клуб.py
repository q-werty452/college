# создайте программу для комп клуба, которая будет спрашивать играл ли этот 1 человек наше игру, если "нет" не играл, тогда регистрируется, он создает себе A a если пароль записываем K себе спиСОК, ЛОГин И пароль, ƏTOT логин он скажет, что у нас играл, мы проверить свой список клиентов, если он там есть, скажем "Добро пожаловать 8 бойцовский луб", а если нет списке, отправялем его на регистрацию. 2а4 дальше после входа, он может пополнить свой баланс или проверить сколько у него на балансе денег. З# у нашего комп клуба есть тарифы, и может выбрать из этих тарифов, если хватает денег, если хватает денег и он выбирает, то с его баланса снимается


tarif= {

 'З часа': 150,
 '5 часа': 220, 
 '7 часа': 330
}
clients = {
"Agent0o7": {'password':'qwerty', 'balance':300,},
}
def registr():
    login = input("Создайте логин: ")
    password = input("Создайте пароль: ")
    clients[login] = {'password': password, 'balance': 0}
    print("Регистрация успешна!")

def login():
    login = input("Введите логин: ")
    if login in clients:
        password = input("Введите пароль: ")
        if clients[login]['password'] == password:
            print("Добро пожаловать в бойцовский клуб!")

            return login
        else:
            print("Неверный пароль!")
    else:
        print("Пользователь не найден. Пройдите регистрацию.")
    return None

def show_balance(login):
    print(f"Ваш баланс: {clients[login]['balance']} сом.")

def add_balance(login):
    amount = int(input("Введите сумму: "))
    clients[login]['balance'] += amount

def buy_tarif(login):
    print("\nДоступные тарифы:")
    for t, price in tarif.items():
        print(f"{t}: {price} сом.")
    choice = input("Выберите тариф: ")
    if choice in tarif:
        if clients[login]['balance'] >= tarif[choice]:
            clients[login]['balance'] -= tarif[choice]
            print("Тариф активирован!")
        else:
            print("Недостаточно средств!")

while True:
    played = input("Вы играли у нас раньше? (да/нет): ")
    
    if played.lower() == "нет":
        registr()
    
    user = login()
    if user:
        while True:
            chois = input("1 - Пополнить баланс\n2 - Проверить баланс\n3 - Выбрать тариф\n4 - Выход\nВыберите действие: ")
            if chois == "1":
                add_balance(user)
            elif chois == "2":
                show_balance(user)
            elif chois == "3":
                buy_tarif(user)
            elif chois == "4":
                break

