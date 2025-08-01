#!/usr/bin/env python3
"""Module that provides a function returning a multiplier
function with type annotations."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes
        a float and returns a float.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
