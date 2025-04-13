import json
import os
from typing import List, Optional


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует объект продукта.
        """
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity

    def __str__(self) -> str:
        """
        Возвращает строку
        """
        return f"{self.name}, {self.description}, Цена: {self.price}, Количество: {self.quantity}"


class Category:
    category_count: int = 0  # Общее количество категорий
    product_count: int = 0    # Общее количество продуктов

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        """
        Инициализирует объект категории
        """
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию и обновляет общее количество товаров
        """
        self.products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """
        Сроку возвращает
        """
        return f"Категория: {self.name}, Описание: {self.description}, Продукты: {len(self.products)}"


def load_data_from_json(file_path: str) -> List[Category]:
    """
    Загрузка с json + создание объектов
    """
    categories = []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for category_data in data:
            products = [
                Product(
                    name=product['name'],
                    description=product['description'],
                    price=product['price'],
                    quantity=product['quantity']
                )
                for product in category_data['products']
            ]

            category = Category(
                name=category_data['name'],
                description=category_data['description'],
                products=products
            )
            categories.append(category)

    return categories


if __name__ == "__main__":
    json_file_path = os.path.join(os.path.dirname(__file__), '../products.json')

    try:
        categories = load_data_from_json(json_file_path)

        for category in categories:
            print(category)
            for product in category.products:
                print(product)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
