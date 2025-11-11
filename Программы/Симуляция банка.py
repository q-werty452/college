class Person:
    def __init__(self, name, age, balance=0):
        self.name = name
        self.age = age
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
    def info(self):
        return f"Клиент: {self.name}, Возраст: {self.age}, Баланс: {self.balance}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.products = []
        self.income = 0
    
    def add_client(self, client):
        self.clients.append(client)
    
    def add_product(self, product):
        self.products.append(product)
    
    def calculate_total_profit(self):
        total = 0
        for product in self.products:
            if hasattr(product, 'calculate_interest'):
                total += product.calculate_interest()
        return total

class BankProduct:
    def __init__(self, client, amount, interest_rate, term_months):
        self.client = client
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_months = term_months
    
    def calculate_interest(self):
        return self.amount * (self.interest_rate / 100) * (self.term_months / 12)
    
    def info(self):
        return f"Клиент: {self.client.name}, Сумма: {self.amount}, Ставка: {self.interest_rate}%"

class Deposit(BankProduct):
    def close_deposit(self):
        interest = self.calculate_interest()
        total = self.amount + interest
        if self.client.deposit(total):
            return True
        return False

class Credit(BankProduct):
    def monthly_payment(self):
        total = self.amount + self.calculate_interest()
        return total / self.term_months
    
    def close_credit(self):
        total = self.amount + self.calculate_interest()
        if self.client.withdraw(total):
            return True
        return False

class Installment:
    def __init__(self, client, product_name, amount, term_months, commission_rate):
        self.client = client
        self.product_name = product_name
        self.amount = amount
        self.term_months = term_months
        self.commission_rate = commission_rate
    
    def monthly_payment(self):
        commission = self.amount * (self.commission_rate / 100)
        total = self.amount + commission
        return total / self.term_months
    
    def close_installment(self):
        total = self.amount + (self.amount * self.commission_rate / 100)
        if self.client.withdraw(total):
            return True
        return False

# Пример использования:
if __name__ == "__main__":
    # Создаем банк
    bank = Bank("МойБанк")
    
    # Создаем клиента
    client = Person("Иван", 30, 100000)
    bank.add_client(client)
    
    # Создаем депозит
    deposit = Deposit(client, 50000, 5, 12)  # 5% годовых на 12 месяцев
    bank.add_product(deposit)
    
    # Создаем кредит
    credit = Credit(client, 100000, 10, 24)  # 10% годовых на 24 месяца
    bank.add_product(credit)
    
    # Создаем рассрочку
    installment = Installment(client, "Телефон", 50000, 6, 2)  # 2% комиссия на 6 месяцев
    
    # Выводим информацию
    print(client.info())
    print(f"Ежемесячный платеж по кредиту: {credit.monthly_payment():.2f}")
    print(f"Ежемесячный платеж по рассрочке: {installment.monthly_payment():.2f}")
    print(f"Общая прибыль банка: {bank.calculate_total_profit():.2f}")