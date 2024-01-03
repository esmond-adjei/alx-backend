#!/usr/bin/env python3
"""
FIFO caching: FIFOCache class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines:
    - put: adds to fifo cache
    - get: get item from fifo cache
    """
    def __init__(self):
        super().__init__()
        self.fifo_table = []

    def put(self, key, item):
        """
        adds item to fifo cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.fifo_table:
            first = self.fifo_table.pop(0)
            del self.cache_data[first]
            print("DISCARD:", first)
        self.fifo_table.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        gets item from fifo cache
        """
        return self.cache_data.get(key)
