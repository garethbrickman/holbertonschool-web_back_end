#!/usr/bin/env python3
""" Annotates function params and return values """

from typing import Dict


# The types of the elements of the input are not know
def safely_get_value(dct, key, default = None):
    """ Duck-typing """
    if key in dct:
        return dct[key]
    else:
        return default