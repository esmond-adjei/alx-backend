#!/usr/bin/env python3
"""
LRU caching: LRUCache class
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines:
    - put: adds to lru cache
    - get: get item from lru cache
    """
    def __init__(self):
        super().__init__()
        self.lru_table = {}

    def put(self, key, item):
        """
        adds item to lru cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.lru_table:
            print(self.lru_table)
            least_recent = min(self.lru_table, key=lambda x: self.lru_table[x])
            del self.cache_data[least_recent]
            del self.lru_table[least_recent]
            print("DISCARD:", least_recent)
        self.lru_table[key] = self.lru_table.get(key, 0)
        self.cache_data[key] = item

    def get(self, key):
        """
        gets item from lru cache
        """
        if self.lru_table.get(key):
            self.lru_table[key] += 1
        return self.cache_data.get(key)
