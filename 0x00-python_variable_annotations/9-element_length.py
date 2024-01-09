#!/usr/bin/env python3
'''
Let's duck type an iterable object
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Computes the length of each element in the input list
    of sequences.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where
        each tuple contains a sequence from the input and
        its corresponding length.
    '''
    return [(i, len(i)) for i in lst]
