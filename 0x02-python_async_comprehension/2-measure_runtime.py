#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run time for four parallel comprehensions

    Returns:
        _type_: time
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    elapsed_time = time.perf_counter() - start_time
    return elapsed_time
