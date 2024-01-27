#!/usr/bin/env python3
"""Module to fetch data within a range"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range - Helper function to specify index
    @page: Int, Page to calculate index for
    @page_size: Int, size of each page
    Returns: Tuple containing indices
    """
    start_idx = (page - 1) * page_size
    return (start_idx, start_idx + page_size)
