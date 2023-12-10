#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_product():
    """
    Запросить данные о продукте.
    """
    name_of_product = input("Имя товара: ")
    name_of_market = input("Имя магазина: ")
    value = int(input("Стоимость товара: "))

    return {
        'name_of_product':name_of_product,
        'name_of_market':name_of_market,
        'value':value
    }