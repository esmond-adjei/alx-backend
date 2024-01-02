#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Gets a total of `page_size` items starting from `index`
        """
        assert type(index) == int and index > 0, \
            "index should be a positive integer"
        total_pages = math.ceil(len(self.__dataset) / page_size)
        assert 0 <= index < total_pages, \
            "index out of range"
        assert type(page_size) == int and page_size > 0, \
            "page_size should be a positive integer"

        page_initial_data = self.__indexed_dataset.get(index, None)
        start_index = index if page_initial_data else index + 1
        next_index = index + page_size
        data = self.__dataset[index: next_index]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
