#!/usr/bin/env python3
'''
Complex types - string and int/float to tuple
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Takes a string k and an int OR float v and returns a tuple.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value (int or float).

    Returns:
        Tuple[str, float]: A tuple containing
        the string key and the square of the value (annotated
        as a float).
    '''
    return k, v ** 2
