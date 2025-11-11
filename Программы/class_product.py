from datetime import date
from typing import Union

# class_product.py



class Product:
    """Базовый класс товара."""
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def buy(self, amount: int) -> bool:
        """Уменьшает количество товара при покупке, если хватает на складе.
        Возвращает True при успешной покупке, False — если недостаточно.
        """
        if amount <= 0:
            raise ValueError("amount должен быть положительным числом")
        if amount > self.quantity:
            print("Недостаточно товара на складе")
            return False
        self.quantity -= amount
        print(f"Покупка выполнена: {amount} шт. товара '{self.name}'")
        return True

    def show_info(self) -> None:
        """Выводит информацию о товаре."""
        print(f"Название: {self.name}")
        print(f"Цена: {self.price}")
        print(f"Количество на складе: {self.quantity}")


class FoodProduct(Product):
    """Товар питания с указанием срока годности."""
    def __init__(self, name: str, price: float, quantity: int, expiration_date: Union[str, date]):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def show_expiration(self) -> None:
        """Выводит срок годности товара."""
        print(f"Срок годности '{self.name}': {self.expiration_date}")


class ElectronicsProduct(Product):
    """Электронный товар с гарантией в годах."""
    def __init__(self, name: str, price: float, quantity: int, warranty_years: int):
        super().__init__(name, price, quantity)
        self.warranty_years = int(warranty_years)

    def show_warranty(self) -> None:
        """Выводит срок гарантии."""
        print(f"Гарантия на '{self.name}': {self.warranty_years} год(а/лет)")