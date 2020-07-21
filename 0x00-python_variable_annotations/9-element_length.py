#!/usr/bin/env python3
""" Annotates function params and return values """

from typing import List, Tuple


def element_length(lst):
    """ Duck-typing """
    return [(i, len(i)) for i in lst]
