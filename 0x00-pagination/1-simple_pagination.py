#!/usr/bin/env python3
"""Module for simple pagination"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range - Helper function to specify index
    @page: Int, Page to calculate index for
    @page_size: Int, size of each page
    Returns: Tuple containing indices
    """
    start_idx = (page - 1) * page_size
    return (start_idx, start_idx + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_page - Gets the specified pages from csv file
        @page: Page to fetch
        @page_size: Size of page to fetch
        Returns: List of pages to fetch
        """
        for in_val in [page, page_size]:
            assert isinstance(in_val, int)
            assert in_val > 0
        (start_idx, end_idx) = index_range(page, page_size)
        dataset_val = self.dataset()
        if end_idx > len(dataset_val):
            return []
        return dataset_val[start_idx:end_idx]
