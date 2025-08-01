#!/usr/bin/env python3
"""Module that measures total runtime for running
async comprehensions in parallel."""

import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime for running 4 async comprehensions in parallel.

    Returns:
        float: Total time in seconds it took to run them.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
