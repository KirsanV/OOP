import unittest

from src.func_category_product import Category, Product


class TestProduct(unittest.TestCase):
    """Тест на правильную инициализацию класса Product"""

    def test_product_initialization(self) -> None:
        """Проверяет инициализацию объекта Product."""
        product: Product = Product(name="Test Product", description="Test Description", price=10.0, quantity=5)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.quantity, 5)


class TestCategory(unittest.TestCase):
    """Тест на правильную инициализацию класса Category"""

    def test_category_initialization(self) -> None:
        """Проверяет инициализацию объекта Category."""
        category: Category = Category(name="Test Category", description="Test Description")
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Test Description")
        self.assertEqual(len(category.products), 0)  # Проверяем, что изначально продуктов нет

    def test_category_count(self) -> None:
        """Подсчет количества категорий"""
        initial_count: int = Category.category_count
        category1: Category = Category(name="Category 1", description="Description 1")
        category2: Category = Category(name="Category 2", description="Description 2")

        self.assertEqual(Category.category_count, initial_count + 2)

    def test_product_count(self) -> None:
        """Подсчет количества продуктов"""
        category: Category = Category(name="Category with Products", description="Description")

        product1: Product = Product(name="Product 1", description="Description 1", price=10.0, quantity=5)
        product2: Product = Product(name="Product 2", description="Description 2", price=20.0, quantity=3)

        category.add_product(product1)
        category.add_product(product2)

        self.assertEqual(Category.product_count, 2)
