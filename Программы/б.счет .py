class BankAccount:
    def __init__(self, owner: str, pin_code, balance: float = 0.0):
        self.__owner = owner
        self.__pin_code = str(pin_code)
        self.__balance = float(balance)

    def get_balance(self, pin):
        """Возвращает баланс при правильном пин-коде."""
        if str(pin) != self.__pin_code:
            raise ValueError("Неверный пин-код")
        return self.__balance

    def deposit(self, dengi):
        """Пополнение счёта (не требует пин-кода)."""
        amount = float(dengi)
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount
        return self.__balance

    def withdraw(self, dengi, pin):
        """Снятие денег при правильном пин-коде и достаточном балансе."""
        if str(pin) != self.__pin_code:
            raise ValueError("Неверный пин-код")
        amount = float(dengi)
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        return self.__balance

    def change_pin(self, old_pin, new_pin):
        """Смена пин-кода при подтверждении старого."""
        if str(old_pin) != self.__pin_code:
            raise ValueError("Неверный старый пин-код")
        self.__pin_code = str(new_pin)
        return True

    def info(self):
        """Выводит имя владельца и закрытый баланс (например, 'Баланс: **** сом')."""
        masked = "****"
        return f"{self.__owner}: Баланс: {masked} сом"