#!/usr/bin/env python3
"""Module that defines an asynchronous coroutine that
waits for a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds
    and return the delay.

    Args:
        max_delay (int): Maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual time waited before returning.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
