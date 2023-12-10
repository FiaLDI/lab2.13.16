#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rectangle import rectangle
from triangle import triangle


def search_area(type = 0):
    '''
    Функция вычисления плозади.
    '''
    
    
    if type == 0:
        return triangle
    else:
        return rectangle