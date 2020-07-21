#!/usr/bin/env python3
""" Annotates function params and return values """

from typing import List, Tuple


# The types of the elements of the input are not know
def safe_first_element(lst):
    """ Duck-typing """
    if lst:
        return lst[0]
    else:
        return None
