#!/usr/bin/env python3
'''
Type Checking
'''

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Zooms in on the elements of a tuple by repeating
    them according to the specified factor.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The factor by which
        to zoom in. Defaults to 2.

    Returns:
        List: A list containing the elements of the input
        tuple repeated according to the specified factor.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
