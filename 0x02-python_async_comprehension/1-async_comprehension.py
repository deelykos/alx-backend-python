#!/usr/bin/env python3
"""1. Async Comprehensions"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """10 random numbers from the async generator

    Returns:
        List[float]: return the 10 random numbers
        from the async generator
    """
    return [i async for i in async_generator()]
