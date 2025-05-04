from abc import ABC, abstractmethod
from typing import List, Optional


class LoggingMixin:
    """
    Миксин для логирования создания объектов
    """

    def __init__(self, *args, **kwargs) -> None:
        class_name = self.__class__.__name__
        params = ', '.join(repr(arg) for arg in args)
        params += ', ' + ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        print(f"Создан объект {class_name} с параметрами: {params}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity


class Product(LoggingMixin, BaseProduct):
    """
    Инициализирует объект продукта.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)
        self.__price = price

    @classmethod
    def new_product(cls, product_data: dict) -> 'Product':
        """
        Создание объекта класса Product
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    @property
    def price(self) -> float:
        """
        Геттер получения цены продукта
        """
        return self.__price

    @price.setter
    def price(self, qwe: float) -> None:
        """
        Сеттер установки цены продукта с проверкой условий
        """
        if qwe <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if hasattr(self, '_Product__price') and qwe < self.__price:
            confirm = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {qwe}? (y/n): ")
            if confirm.lower() != 'y':
                return
        self.__price = qwe

    def __str__(self) -> str:
        """
        Возвращает строкуL Название продукта, Xруб, Остаток: X шт.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, second_arg: 'Product') -> float:
        """

        return (self.price * self.quantity) + (second_arg.price * second_arg.quantity)


class Category:
    """
    Инициализирует объект категории.
    """
    product_counter = 0
    category_counter = 0

    def __init__(self, name: str, description: str, products: Optional[List[BaseProduct]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[BaseProduct] = products if products is not None else []
        Category.category_counter += 1

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию и считает количество добавленных продуктов.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять продукты только одного типа")

        self.__products.append(product)
        Category.product_counter += 1

    @property
    def products(self) -> List[BaseProduct]:
        """
        Гетер задает нужный формат по заданию
        """
        return self.__products

    @property
    def product_count(self) -> int:
        """
        Считает количество продуктов в списке
        """
        return len(self.__products)

    def __str__(self) -> str:
        """
        Возвращает строку: Название категории, количество продуктов: X шт
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

