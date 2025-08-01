#!/usr/bin/env python3
"""Module that defines a function to create an asyncio.Task for wait_random."""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task that wraps wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A Task object that will run wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
