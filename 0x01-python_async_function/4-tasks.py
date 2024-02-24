#!/usr/bin/env python3
"""Tasks"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute multiple coroutines at the same time with async"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    list_of_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        list_of_delays.append(delay)
    return sorted(list_of_delays)
