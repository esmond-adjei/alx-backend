#!/usr/bin/env python3
"""
LIFO caching: LIFOCache class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines:
    - put: adds to lifo cache
    - get: get item from lifo cache
    """
    def __init__(self):
        super().__init__()
        self.lifo_table = []

    def put(self, key, item):
        """
        adds item to lifo cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.lifo_table:
            first = self.lifo_table.pop()
            del self.cache_data[first]
            print("DISCARD:", first)
        self.lifo_table.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        gets item from lifo cache
        """
        return self.cache_data.get(key)
