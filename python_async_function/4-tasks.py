#!/usr/bin/env python3
"""Module that runs multiple task-based coroutines concurrently."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return
    list of results in ascending order.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)
    return delays
