#!/usr/bin/env python3
"""Module that provides a function to return a tuple
of a string and the square of a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number as a float.

    Args:
        k (str): A string key.
        v (int or float): A numeric value.

    Returns:
        Tuple[str, float]: A tuple with the key and the squared
        value as a float.
    """
    return (k, float(v ** 2))
