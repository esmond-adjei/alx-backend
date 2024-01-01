#!/usr/bin/env python3
"""
Simple Helper Function For Pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start index and end index for a given
    page and page_size
    """
    return (page_size * (page - 1), page_size * page)
