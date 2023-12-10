#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select_products(products, find_name):
    """
    Выбрать продукт с заданным именем.
    """
    result = []
    for product in products:
        if product.get('name_of_product') == find_name:
            result.append(product)

    return result