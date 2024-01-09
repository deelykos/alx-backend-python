#!/usr/bin/env python3
'''
More involved type annotations
'''

from typing import Mapping, Any, Union, TypeVar


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None
                     ) -> Union[Any, T]:
    '''
    Safely gets a value from a dictionary based on the given key.

    Args:
        dct (Mapping): The input mapping (dictionary-like object).
        key (Any): The key to look up in the mapping.
        default (Union[T, None], optional): The default value
        to return if the key is not found.
        Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the
        key, or the default value if the key is not present.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
