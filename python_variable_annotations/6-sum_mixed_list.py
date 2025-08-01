#!/usr/bin/env python3
"""Module that provides a function to sum a mixed
list of ints and floats with type annotations."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The total sum as a float.
    """
    return sum(mxd_lst)
