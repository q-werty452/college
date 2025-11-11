class Car:
    def __init__(self, brand, year, model, speed, cost):
        self.brand = brand
        self.year = year
        self.model = model
        self.speed = speed
        self.cost = cost
        self.going = False

    def car_is_started(self, kmH):
        self.speed = kmH
        self.going = True
        print(f"{self.brand} поехала со скоростью {self.speed} км/ч.Состояние: {self.going}")

    def car_is_stopped(self, kmH):
        self.speed = 0
        self.going = False
        print(f"{self.brand} остановилась.")

    def info(self):
        print(f"Бренд: {self.brand}, Модель: {self.model}, Год: {self.year}, Скорость: {self.speed} км/ч, Стоимость: {self.cost}")
car1 = Car("Toyota", 2020, "Camry", 120, 30000)
car2 = Car("Honda", 2019, "Accord", 130, 28000)
car3 = Car("Ford", 2018, "Focus", 140, 25000)
car1.info()
car2.info()
car3.info()
car1.car_is_started(100)