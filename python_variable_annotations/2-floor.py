#!/usr/bin/env python3
"""Module that provides a function to compute the floor
of a float with type annotations."""

import math


def floor(n: float) -> int:
    """Return the floor of a float.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of n.
    """
    return math.floor(n)
