#!/usr/bin/env python3
"""Module that measures the average runtime of wait_n."""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure average execution time per coroutine for wait_n.

    Args:
        n (int): Number of times to run wait_random concurrently.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
