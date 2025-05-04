import unittest
from unittest.mock import patch

from src.func_category_product import BaseProduct, Category, LawnGrass, Product, Smartphone


class TestProduct(unittest.TestCase):
    """Тесты для класса Product"""

    def test_product_initialization_with_zero_quantity(self) -> None:
        """Проверяет можно ли добавить продуктс нулевым количеством"""
        with self.assertRaises(ValueError) as context:
            Product(name="Чых", description="Пых", price=123.0, quantity=0)
        self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен")

    def test_product_initialization_with_negative_quantity(self) -> None:
        """Проверяет можно ли добавить продукт с отрицаетльным количеством"""
        with self.assertRaises(ValueError) as context:
            Product(name="Чых", description="Пых", price=123.0, quantity=-532543453453453465645)
        self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен")

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

    def setUp(self) -> None:
        """Собирает сет для тестов"""
        self.category = Category(name="Test Category", description="Test Description")
        self.product1 = Product(name="Product 1", description="Description 1", price=100.0, quantity=10)
        self.product2 = Product(name="Product 2", description="Description 2", price=200.0, quantity=5)

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

    def test_middle_price_with_products(self) -> None:
        """Считает среднюю цену на продукты"""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)

        expected_middle_price = (self.product1.price * self.product1.quantity +
                                 self.product2.price * self.product2.quantity) / \
                                (self.product1.quantity + self.product2.quantity)

        self.assertAlmostEqual(self.category.middle_price(), expected_middle_price)

    def test_middle_price_with_no_products(self) -> None:
        """Возвращает ноль, если продуктов нет"""
        self.assertEqual(self.category.middle_price(), 0)


class TestSmartphone(unittest.TestCase):

    def test_smartphone_initialization(self) -> None:
        """Проверяет инициализацию объекта Smartphone"""
        smartphone = Smartphone(
            name="iPhone 16",
            description="Лучший смартфон от Apple",
            price=210000.0,
            quantity=50,
            efficiency=95.0,
            model="A2649",
            memory=128,
            color="черный"
        )
        self.assertEqual(smartphone.name, "iPhone 16")
        self.assertEqual(smartphone.description, "Лучший смартфон от Apple")
        self.assertEqual(smartphone.price, 210000.0)
        self.assertEqual(smartphone.quantity, 50)
        self.assertEqual(smartphone.efficiency, 95.0)
        self.assertEqual(smartphone.model, "A2649")
        self.assertEqual(smartphone.memory, 128)
        self.assertEqual(smartphone.color, "черный")

    def test_smartphone_str(self) -> None:
        """Проверяет вывод строки для смартфона"""
        smartphone = Smartphone(
            name="Samsung Galaxy S24",
            description="Флагман от Samsung",
            price=250000.0,
            quantity=30,
            efficiency=90.0,
            model="SM-G991B",
            memory=256,
            color="синий"
        )
        expected_output = "Samsung Galaxy S24, 250000.0 руб. Остаток: 30 шт."
        self.assertEqual(str(smartphone), expected_output)


class TestLawnGrass(unittest.TestCase):

    def test_lawn_grass_initialization(self) -> None:
        """Проверяет инициализацию объекта LawnGrass"""
        lawn_grass = LawnGrass(
            name="Газонная трава",
            description="Полынь",
            price=25.0,
            quantity=100,
            country="Россия",
            germination_period="7-14 дней",
            color="зеленый"
        )
        self.assertEqual(lawn_grass.name, "Газонная трава")
        self.assertEqual(lawn_grass.description, "Полынь")
        self.assertEqual(lawn_grass.price, 25.0)
        self.assertEqual(lawn_grass.quantity, 100)
        self.assertEqual(lawn_grass.country, "Россия")
        self.assertEqual(lawn_grass.germination_period, "7-14 дней")
        self.assertEqual(lawn_grass.color, "зеленый")

    def test_lawn_grass_str(self) -> None:
        """Проверяет вывод строки для газонной травы"""
        lawn_grass = LawnGrass(
            name="Газончик",
            description="Готовый газон в рулонах",
            price=321.0,
            quantity=123,
            country="США",
            germination_period="10-15 дней",
            color="зеленый"
        )
        expected_output = "Газончик, 321.0 руб. Остаток: 123 шт."
        self.assertEqual(str(lawn_grass), expected_output)


class TestLoggingMixin(unittest.TestCase):
    """Тесты для проверки работы миксина логирования."""

    @patch('builtins.print')
    def test_logging_mixin(self, mock_print: unittest.mock.Mock) -> None:
        """
        Проверяет, что при создании объекта Product вызывается
        функция print с ожидаемым сообщением.
        """
        product = Product("Тестовый продукт", "Описание продукта", 100.0, 10)
        mock_print.assert_called_once()
        call_args = mock_print.call_args[0][0]
        expected_output = "Создан объект Product с параметрами: 'Тестовый продукт', 'Описание продукта', 100.0, 10, "
        self.assertEqual(call_args, expected_output)
        self.assertEqual(product.name, "Тестовый продукт")
        self.assertEqual(product.description, "Описание продукта")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.quantity, 10)


class TestBaseProduct(unittest.TestCase):

    class ConcreteProduct(BaseProduct):
        """Реализация абстрактного класса BaseProduct"""

        def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
            """
            Инициализирует объект
            """
            super().__init__(name, description, price, quantity)
            self.price = price

    def test_base_product_initialization(self) -> None:
        """
        Проверяет корректность инициализации объекта
        """
        product = self.ConcreteProduct("Test Product", "Description", 10.0, 5)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.quantity, 5)

    def test_base_product_abstract_class(self) -> None:
        """
        Проверяет, что попытка создать экземпляр абстрактного класса BaseProduct
        вызывает исключение TypeError
        """
        with self.assertRaises(TypeError):
            BaseProduct("Test Product", "Description", 10.0, 5)
