#!/usr/bin/env python3
"""Module that provides a function to concatenate two strings with
type annotations."""


def concat(str1: str, str2: str) -> str:
    """Return the concatenation of two strings.

    Args:
        str1 (str): First string.
        str2 (str): Second string.

    Returns:
        str: The concatenated result of str1 and str2.
    """
    return str1 + str2
