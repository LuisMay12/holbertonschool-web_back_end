#!/usr/bin/env python3
"""Hypermedia pagination over Popular_Baby_Names.csv."""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute the start and end indices for a paginated slice.

    Given a 1-indexed page number and a page size, return a tuple
    (start, end) suitable for slicing a list, where `start` is inclusive
    and `end` is exclusive.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: List[List] | None = None

    def dataset(self) -> List[List]:
        """Return the cached dataset (header removed)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.

        Raises:
            AssertionError: if page or page_size are not positive integers.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return hypermedia pagination info for a given page.

        The dictionary includes:
            - page_size: length of the returned page (may be 0)
            - page: current page number
            - data: list of rows for this page
            - next_page: next page number or None
            - prev_page: previous page number or None
            - total_pages: total number of pages
        """

        data_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size) if total_items else 0

        return {
            "page_size": len(data_page),          # 0 if out of range
            "page": page,
            "data": data_page,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
