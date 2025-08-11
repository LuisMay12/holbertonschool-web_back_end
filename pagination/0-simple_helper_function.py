#!/usr/bin/env python3
"""Helper utilities for pagination."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute the start and end indices for a paginated slice.

    Given a 1-indexed page number and a page size, return a tuple
    (start, end) suitable for slicing a list, where `start` is inclusive
    and `end` is exclusive.

    Example:
        page=1, page_size=7  -> (0, 7)
        page=3, page_size=15 -> (30, 45)

    Args:
        page: The current page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple (start, end) with zero-based indices.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
