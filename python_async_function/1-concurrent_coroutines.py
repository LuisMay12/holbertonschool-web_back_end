#!/usr/bin/env python3
"""Module that defines an async routine to
run multiple coroutines concurrently."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the
    specified max_delay.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Max delay for each coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    for coro in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await coro
        delays.append(delay)
    return delays
