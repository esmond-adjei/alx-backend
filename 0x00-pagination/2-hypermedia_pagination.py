#!/usr/bin/env python3
"""
Simple Helper Function For Pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Union, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start index and end index for a given
    page and page_size
    """
    return (page_size * (page - 1), page_size * page)


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
        Gets items for the given page and page_size
        """
        assert type(page) == int and page > 0, \
            "page should be positive integer"
        assert type(page_size) == int and page_size > 0, \
            "page_size should be positive integer"
        start_index, end_index = index_range(page, page_size)
        if self.__dataset is None:
            self.dataset()
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, Union[int, List[Union[int, str]], Optional[int]]]:
        """
        Gets items for a given page and page_size with hypermedia
        for next_page, and prev_page
        """
        data = self.get_page(page, page_size)
        has_next = data != []
        has_prev = page > 1
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if has_next else None,
            'prev_page': page - 1 if has_prev else None,
            'total_pages': math.ceil(len(self.__dataset) / page_size),
        }
