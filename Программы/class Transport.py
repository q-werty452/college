class Transport:
    def __init__(self,  speed, capacity):
        self.speed = speed
        self.capacity = capacity

class Car(Transport):
    def car_is_started(self, kmH, brand, model, year, cost , capacity):
        self.speed = kmH
        self.going = True
        self.brand = brand
        self.model = model
        self.year = year
        self.cost = cost
        self.capacity = capacity
        print(f"Машина {self.brand} с вместительностью {self.capacity} поехала со скоростью {self.speed} км/ч. Состояние: {self.going}")

    def car_is_stopped(self, kmH):
        self.speed = 0
        self.going = False
        print(f"Машина {self.brand} остановилась.")

    def info(self):
        print(f"Бренд: {self.brand}, Модель: {self.model}, Год: {self.year}, Скорость: {self.speed} км/ч, Стоимость: {self.cost}")

class Electryc(Transport):
    class Electryc:
        def __init__(self, battery_level=100):
            self._battery_level = battery_level

        def charge(self):
            self._battery_level = 100
            print("Батарея заряжена до 100%.")

        def battery_status(self):
            print(f"Уровень заряда батареи: {self._battery_level}%")
            return self._battery_level

        def info(self):
            super().info()
            print(f"Уровень заряда батареи: {self._battery_level}%")



car1 = Car("Toyota", 2020, "Camry", 120, 30000, "5 мест", )
car2 = Car("Honda", 2019, "Accord", 130, 28000, "5 мест")
car3 = Car("Ford", 2018, "Focus", 140, 25000, "5 мест")
car1.info()
car2.info()
car3.info()
car1.car_is_started(100)