from typing import List, Optional


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализирует объект продукта.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
        Инициализирует объект категории.
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию и обновляет общее количество товаров.
        """
        self.products.append(product)
        Category.product_count += 1
