#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def display_products(workers):
    """
    Отобразить список работников.
    """
    if workers:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 10
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^10} |'.format(
                "№",
                "Название продукта",
                "Имя магазина",
                "Стоимость"
            )
        )
        print(line)
        for idx, worker in enumerate(workers, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>10} |'.format(
                    idx,
                    worker.get('name_of_product', ''),
                    worker.get('name_of_market', ''),
                    worker.get('value', 0)
                )
            )
        print(line)
       
    else:
        print("Список продуктов пуст.")