import json
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from src.processing_with_json import Category, Product, load_data_from_json


def test_product_initialization() -> None:
    """Инициализация класса продукта проверка"""

    product: Product = Product("Товар 1", "Описание товара 1", 100.0, 10)
    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization() -> None:
    """Инициализация класса категории проверка"""

    category: Category = Category("Категория 1", "Описание категории 1")
    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert len(category.products) == 0


def test_add_product_to_category() -> None:
    """Проверка добавления продукта в определённую категорию"""

    category: Category = Category("Категория 1", "Описание категории 1")
    product: Product = Product("Товар 1", "Описание товара 1", 100.0, 10)

    category.add_product(product)

    assert len(category.products) == 1
    assert category.products[0] == product


def test_load_data_from_json() -> None:
    """Грузим файлы из json формата проверка"""

    mock_data: List[Dict[str, Any]] = [
        {
            "name": "Категория 1",
            "description": "Описание категории 1",
            "products": [
                {"name": "Товар 1", "description": "Описание товара 1", "price": 100.0, "quantity": 10},
                {"name": "Товар 2", "description": "Описание товара 2", "price": 200.0, "quantity": 5}
            ]
        },
        {
            "name": "Категория 2",
            "description": "Описание категории 2",
            "products": []
        }
    ]

    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        categories: List[Category] = load_data_from_json("fake_path.json")

        assert len(categories) == 2

        assert categories[0].name == "Категория 1"
        assert len(categories[0].products) == 2

        assert categories[0].products[0].name == "Товар 1"
        assert categories[0].products[0].price == 100.0

        assert categories[1].name == "Категория 2"
        assert len(categories[1].products) == 0
