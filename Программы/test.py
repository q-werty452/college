class Person :
    def __init__(self,name,age,balance):
        self.name=name 
        self.age=age
        self.balance=balance

    def deposit (self , amount):
        if amount > 0: 
            self.dalance += amount
            return True 
        return False 
    
    def withdraw (self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount 
            return True
        return False 
    

    def info (self):
        return f"Клиент: {self.name}, Возраст: {self.age}, Баланс: {self.balance}"
    
class Bank : 
    def __init__ (self, name):
        self.name = name 
        self.clients = []
        self.products = []
        self.income = 0

    def add_client (self, client):
        self.clients.append(client)

    def add_product (self, product):
        self.products.append(product)

    def calculate_total_profit (self):
        total = 0 
        # for product in self.products: 
        #     total += product.price * product.sales
        return total
