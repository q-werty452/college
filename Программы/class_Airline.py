# Система авиабронирования
# создать программу используя классы <инкапсуляция и взаимодействие обьектов
# Программа должа позволять: создовать и удолять рейсы , покупать и отменять билеты, изменять параметры рейса , расчитывать общую выручку ,показывать статистику.add()
# класс Flight : Отвечает за конкретный рейс . Содержит : направления (rout),количества мест эканом и бизнес , цены , количество проданных билетов , методы добавления, удоления ,поиска и статистики
# класс Client , Сохроняет данные клиента и купленного билета .

class Flight:
    def __init__(self, route, econ_seats, biz_seats, econ_price, biz_price):
        self.route = route
        self.econ_seats = econ_seats
        self.biz_seats = biz_seats
        self.econ_price = econ_price
        self.biz_price = biz_price
        self.sold_econ_tickets = 0
        self.sold_biz_tickets = 0

    def add_seats(self, econ, biz):
        self.econ_seats += econ
        self.biz_seats += biz

    def remove_seats(self, econ, biz):
        if econ <= self.econ_seats and biz <= self.biz_seats:
            self.econ_seats -= econ
            self.biz_seats -= biz
        else:
            print("Недостаточно мест для удаления")

    def sell_ticket(self, seat_type):
        if seat_type == 'econ' and self.econ_seats > 0:
            self.econ_seats -= 1
            self.sold_econ_tickets += 1
            # скидка 5% если продано более 5 билетов эконом класса
            if self.sold_econ_tickets > 5:
                return int(self.econ_price * 0.95)
            return self.econ_price
        elif seat_type == 'biz' and self.biz_seats > 0:
            self.biz_seats -= 1
            self.sold_biz_tickets += 1
            # скидка 10% если продано более 2 билетов бизнес класса
            if self.sold_biz_tickets > 2:
                return int(self.biz_price * 0.9)

            return self.biz_price
        else:
            print("Нет доступных мест данного типа")
            return 0

    def cancel_ticket(self, seat_type):
        if seat_type == 'econ' and self.sold_econ_tickets > 0:
            self.econ_seats += 1
            self.sold_econ_tickets -= 1
        elif seat_type == 'biz' and self.sold_biz_tickets > 0:
            self.biz_seats += 1
            self.sold_biz_tickets -= 1
        else:
            print("Нет проданных билетов данного типа для отмены")

    def calculate_revenue(self):
        return (self.sold_econ_tickets * self.econ_price) + (self.sold_biz_tickets * self.biz_price)

    def get_statistics(self):
        return {
            'route': self.route,
            'econ_seats_available': self.econ_seats,
            'biz_seats_available': self.biz_seats,
            'sold_econ_tickets': self.sold_econ_tickets,
            'sold_biz_tickets': self.sold_biz_tickets,
            'total_revenue': self.calculate_revenue()
        }
    
class Client:
    def __init__(self, name, flight, seat_type):
        self.name = name
        self.flight = flight
        self.seat_type = seat_type
        self.ticket_price = flight.sell_ticket(seat_type)

    def cancel_ticket(self):
        self.flight.cancel_ticket(self.seat_type)
        self.ticket_price = 0


q1 = Flight("Москва — Санкт-Петербург", 120, 20, 2500, 7000)
q2 = Flight("Москва — Симферополь", 150, 15, 3000, 8000)
q3 = Flight("Новосибирск — Екатеринбург", 100, 10, 2200, 6000)
q4 = Flight("Казань — Москва", 130, 12, 2700, 7500)

w1 = Client("Иван Иванов", q1, 'econ')
w2 = Client("Ольга Петрова", q2, 'biz')
w3 = Client("Алексей Сидоров", q3, 'econ')
w4 = Client("Мария Кузнецова", q4, 'biz')

for e in (q1, q2, q3, q4):
    print(e.get_statistics())                  


