#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from store.get_product import get_product
from store.display_product import display_products
from store.select_product import select_products
import sys


def main():
    """
    Главная функция программы.
    """
    products = []
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = get_product()
            products.append(product)
            if len(products) > 1:
                products.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            display_products(products)

        elif command.startswith('info '):
            parts = command.split(' ', maxsplit=1)
            find_name = parts[1]
            selected = select_products(products, find_name)
            display_products(selected)

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()