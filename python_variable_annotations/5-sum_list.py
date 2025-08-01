#!/usr/bin/env python3
"""Module that provides a function to sum a list
of floats with type annotations."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.

    Args:
        input_list (List[float]): List containing float numbers.

    Returns:
        float: The total sum of the float numbers in the list.
    """
    return sum(input_list)
