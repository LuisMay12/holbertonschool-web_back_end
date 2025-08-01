#!/usr/bin/env python3
"""Module that annotates a function returning the
lengths of iterable elements."""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence])-> List[Tuple[Sequence, int]]:
    """Return a list of tuples with elements and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        (like str, list, tuple).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing the
        sequence and its length.
    """
    return [(i, len(i)) for i in lst]
