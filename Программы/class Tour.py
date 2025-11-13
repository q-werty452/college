# Каждый тур имеет свою цену, длительность, статус (доступен/забронирован) и клиента, который его купил.
# Клиенты могут просматривать доступные туры, бронировать и оплачивать их.
# Агентство может смотреть общую выручку и управлять турами.

# 1. Класс Tour
# Инкапсулированный класс, представляющий один тур.
# Атрибуты:
# __id — уникальный номер тура (инкапсулированный, доступ только через свойство);
# __price — цена тура (инкапсулированный, управляется через @property);
# _is_booked — защищённый атрибут (True/False);
# _client — текущий клиент или None;
# _days — количество дней тура.

# Методы:
# book(client) — бронирует тур, делает его недоступным, если клиент оплатил.
# cancel_booking() — отменяет бронь, делает тур доступным.
# info() — краткая информация о туре.

# Свойства:
# price — через @property и @setter (цена не может быть ниже 5000 сом).
# id — только для чтения.

# 2. Класс Client
# Атрибуты:
# name — имя клиента;
# balance — баланс клиента.

# Методы:
# pay(amount) — уменьшает баланс, если хватает денег;
# add_balance(amount) — пополнение счёта;
# info() — возвращает строку с именем и балансом.


# 3. Класс Agency
# Атрибуты:
# name — название агентства;
# tours — список объектов Tour;
# _income — защищённый атрибут (доход агентства).

# Методы:
# add_tour(tour) — добавляет новый тур;
# show_available_tours() — показывает все свободные туры;
# book_tour(client, tour_id) — бронирует тур для клиента;
# cancel_all_bookings() — отменяет все активные брони;
# show_status() — показывает состояние всех туров и текущую выручку.

class Tour:
    def __init__(self, tour_id, price, days):
        self.__id = tour_id
        self.__price = price
        self._is_booked = False
        self._client = None
        self._days = days

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 5000:
            raise ValueError("Цена не может быть ниже 5000 сом.")
        self.__price = value

    @property
    def id(self):
        return self.__id

    def book(self, client):
        if not self._is_booked:
            self._is_booked = True
            self._client = client
            return True
        return False

    def cancel_booking(self):
        self._is_booked = False
        self._client = None

    def info(self):
        return f"Тур ID: {self.__id}, Цена: {self.__price}, Дни: {self._days}, Забронирован: {self._is_booked}"

class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def add_balance(self, amount):
        self.balance += amount

    def info(self):
        return f"Клиент: {self.name}, Баланс: {self.balance}"

class Agency:
    def __init__(self, name):
        self.name = name
        self.tours = []
        self._income = 0

    def add_tour(self, tour):
        self.tours.append(tour)

    def show_available_tours(self):
        return [tour.info() for tour in self.tours if not tour._is_booked]

    def book_tour(self, client, tour_id):
        for tour in self.tours:
            if tour.id == tour_id and not tour._is_booked:
                if client.pay(tour.price):
                    tour.book(client)
                    self._income += tour.price
                    return True
        return False

    def cancel_all_bookings(self):
        for tour in self.tours:
            tour.cancel_booking()

    def show_status(self):
        return [(tour.info(), self._income) for tour in self.tours]
         