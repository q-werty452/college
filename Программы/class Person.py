
# 1. Класс Person Базовый класс для людей в ресторане.
# Атрибуты: name, age
# Метод: info() - возвращает строку "Имя: {name}, Возраст: {age}".

# 2. Класс Employee (наследуется от Person)
# Атрибуты: salary, position
# Метод: calculate_salary() - возвращает месячную зарплату.
# info() - расширяет базовый метод: "Имя: {name}, Возраст: {age}, 
# Должность: {position}, Зарплата: {salary}".

# 3. Подклассы сотрудников:
# Chef - повар
# Метод: cook(dish_name) - печатает "Повар {name} готовит {dish_name}".
# Waiter - официант.
# Метод: take_order(dish_list) - создает и возвращает объект класса Order.
# Manager - менеджер.
# Метод: calculate_profit(income, expenses) - возвращает прибыль (income - expenses).

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

class Employee(Person):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age)
        self.salary = salary
        self.position = position
    
    def calculate_salary(self):
        return self.salary
    
    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}, Зарплата: {self.salary}"

class Chef(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary, "Повар")
    
    def cook(self, dish_name):
        print(f"Повар {self.name} готовит {dish_name}")

class Waiter(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary, "Официант")
    
    def take_order(self, dish_list):
        return Order(dish_list) 

class Manager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary, "Менеджер")
    
    def calculate_profit(self, income, expenses):
        return income - expenses


class Order:
    def __init__(self, dish_list):
        self.dish_list = dish_list



waiter = Waiter("Мария", 25, 40000)
manager = Manager("Алексей", 40, 70000)
chef = Chef("Иван", 30, 50000)
print(chef.info())
chef.cook("Борщ")   
order = waiter.take_order(["Борщ", "Пельмени"])
print(f"Официант {waiter.name} принял заказ: {order.dish_list}")
profit = manager.calculate_profit(200000, 150000)
print(f"Прибыль менеджера {manager.name}: {profit}")