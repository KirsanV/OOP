from typing import List, Optional


class Product:
    """
    Инициализирует объект продукта.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        if qwe < self.__price:
            confirm = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {qwe}? (y/n): ")
            if confirm.lower() != 'y':
                return
        self.__price = qwe

    def __str__(self) -> str:
        """
        Возвращает строкуL Название продукта, X руб. Остаток: X шт.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, second_arg: 'Product') -> float:
        """
        Складывает сумму 2ух продуктов
        """
        if not isinstance(second_arg, Product):
            return NotImplemented
        return (self.price * self.quantity) + (second_arg.price * second_arg.quantity)


class Category:
    """
    Инициализирует объект категории.
    """
    product_counter = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию и считает количество добавленных продуктов.
        """
        self.__products.append(product)
        Category.product_counter += 1

    @property
    def products(self) -> str:
        """
        Гетер задает нужный формат по заданию
        """
        return "\n".join(f"{product.name}, {product.price} руб. Остаток: "
                         f"{product.quantity} шт." for product in self.__products)

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
