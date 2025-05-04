import unittest
from unittest.mock import patch

from src.func_category_product import BaseProduct, Category, LawnGrass, Product, Smartphone


class TestProduct(unittest.TestCase):
    """Тесты для класса Product"""

    def test_product_initialization(self) -> None:
        """Проверяет инициализацию объекта Product"""
        product: Product = Product(name="Стиралочка", description="Я стираю ваши вещи, но не грехи", price=1111.0,
                                   quantity=4335)
        self.assertEqual(product.name, "Стиралочка")
        self.assertEqual(product.description, "Я стираю ваши вещи, но не грехи")
        self.assertEqual(product.price, 1111.0)
        self.assertEqual(product.quantity, 4335)

    def test_new_product_class_method(self) -> None:
        """Проверяет создание продукта через метод new_product"""
        product_data: dict[str, str | float | int] = {
            "name": "Какой-то супер продукт",
            "description": "Описание какого-то продукта",
            "price": 15.0,
            "quantity": 10
        }
        product: Product = Product.new_product(product_data)
        self.assertEqual(product.name, "Какой-то супер продукт")
        self.assertEqual(product.description, "Описание какого-то продукта")
        self.assertEqual(product.price, 15.0)
        self.assertEqual(product.quantity, 10)

    def test_price_setter(self) -> None:
        """Проверяет установку цены продукта с условиями"""
        product: Product = Product(name="цццц", description="сссс", price=123.0, quantity=5)
        product.price = 1234.0
        self.assertEqual(product.price, 1234.0)

        with patch('builtins.print') as mock_print:
            product.price = -5.0
            mock_print.assert_called_once_with("Цена не должна быть нулевая или отрицательная")

    def test_price_lowering_confirmation(self) -> None:
        """Проверяет понижение цены с подтвыерждением от юзера"""
        product: Product = Product(name="это нам не нужно", description="и это тоже", price=321.0, quantity=5)

        with patch('builtins.input', return_value='n'):
            product.price = 8.0
            self.assertEqual(product.price, 321.0)

        with patch('builtins.input', return_value='y'):
            product.price = 44444.0
            self.assertEqual(product.price, 44444.0)

    def test_product_str(self) -> None:
        """Проверяет вывод строки"""
        product = Product(name="Смартфон", description="Описание", price=1020.0, quantity=53)
        self.assertEqual(str(product), "Смартфон, 1020.0 руб. Остаток: 53 шт.")

    def test_product_addition(self) -> None:
        """Проверка сложения 2ух продуктов"""
        product1 = Product(name="Продукт 1", description="Описание 1", price=123.0, quantity=123)
        product2 = Product(name="Продукт 2", description="Описание 2", price=456.0, quantity=456)
        total_value = product1 + product2
        self.assertEqual(total_value, (123.0 * 123) + (456.0 * 456))


class TestCategory(unittest.TestCase):
    """Тесты для класса Category"""

    def test_category_initialization(self) -> None:
        """Проверяет инициализацию объекта Category"""
        category: Category = Category(name="Совершенно секретно", description="уауы")
        self.assertEqual(category.name, "Совершенно секретно")
        self.assertEqual(category.description, "уауы")
        self.assertEqual(len(category.products), 0)

    def test_add_product(self) -> None:
        """Добавляет продукт в категорию"""
        category: Category = Category(name="Тополя", description="Траляля")
        product1: Product = Product(name="не особо важно, что здесь будет", description="тртртр", price=10.0,
                                    quantity=5)
        initial_count: int = category.product_count
        category.add_product(product1)
        self.assertEqual(category.product_count, initial_count + 1)

    def test_products_property(self) -> None:
        """Тестим свойство products"""
        category: Category = Category(name="Вообще можно было", description="в константы кинуть это всё")
        product1: Product = Product(name="И не парить себе", description="Мозг писаниной", price=1045.0, quantity=32)
        category.add_product(product1)
        expected_output: str = "И не парить себе, 1045.0 руб. Остаток: 32 шт."
        actual_output = str(category.products[0])

        self.assertEqual(actual_output.strip(), expected_output)

    def test_product_count_property(self) -> None:
        """Тестим свойство produdct_count"""
        category: Category = Category(name="Вымышленный продукт", description="Описание вымышленного продукта")
        self.assertEqual(category.product_count, 0)
        product1: Product = Product(name="Условный продукт", description="с каким-то описанием", price=123789456.0,
                                    quantity=5)
        category.add_product(product1)
        self.assertEqual(category.product_count, 1)

    def test_category_str(self) -> None:
        """тестим вывод строки по классу категория"""
        category = Category(name="Телефоны", description="лучший тлф")
        product1 = Product(name="Продукт Айфон", description="Айфон", price=5000.0, quantity=123)
        product2 = Product(name="Продукт Самсунг", description="Самсунг", price=15000.0, quantity=123)
        category.add_product(product1)
        category.add_product(product2)
        expected_output = "Телефоны, количество продуктов: 246 шт."
        self.assertEqual(str(category), expected_output)


