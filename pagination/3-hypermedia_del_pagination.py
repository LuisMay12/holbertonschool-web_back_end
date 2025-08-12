#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset: Optional[List[List]] = None
        self.__indexed_dataset: Optional[Dict[int, List]] = None

    def dataset(self) -> List[List]:
        """Cached dataset (header removed)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by original position, starting at 0."""
        if self.__indexed_dataset is None:
            data = self.dataset()
            # Index every row by its original position
            self.__indexed_dataset = {i: data[i] for i in range(len(data))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page.

        Args:
            index: starting index requested (0-based). If None, defaults to 0.
            page_size: number of items to return.

        Returns:
            Dict with:
                - index: the requested start index
                - next_index: the next index to query
                - page_size: the number of items actually returned
                - data: the list of rows for this page

        Behavior:
            - Skips missing indices (deleted rows) so the client doesn't miss items.
            - Asserts that `index` is within a valid range.
        """
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0, "index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        indexed = self.indexed_dataset()
        assert index < (len(indexed) if len(indexed) > 0 else 1), "index out of range"

        data: List[List] = []
        current = index
        items_collected = 0

        max_key = max(indexed.keys()) if indexed else -1
        while items_collected < page_size and current <= max_key:
            if current in indexed:
                data.append(indexed[current])
                items_collected += 1
            current += 1

        next_index = current

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
