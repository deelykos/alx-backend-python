#!/usr/bin/env python3
'''
Complex types - list of floats
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Takes a list of floats as an argument and returns their sum.

    Args:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of the input list.
    '''
    return sum(input_list)
