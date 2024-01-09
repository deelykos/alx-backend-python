#!/usr/bin/env python3
'''
Complex types - functions
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Takes a float multiplier as an argument and returns a function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies
        a float by the given multiplier.
    '''
    return lambda value: multiplier * value
