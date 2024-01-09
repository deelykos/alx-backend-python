#!/usr/bin/env python3
'''
Duck typing - first element of a sequence
'''

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Safely retrieves the first element from the given sequence.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence,
        or None if the sequence is empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
