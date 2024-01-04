#!/usr/bin/env python3
"""
LFU caching: LFUCache class
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines:
    - put: adds to lfu cache
    - get: get item from lfu cache
    """
    def __init__(self):
        super().__init__()
        self.lfu_table = {}

    def put(self, key, item):
        """
        adds item to lfu cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                item_discarded = min(self.lfu_table, key=self.lfu_table.get)
                self.lfu_table.pop(item_discarded)
                self.cache_data.pop(item_discarded)
                print("DISCARD:", item_discarded)
            self.lfu_table[key] = self.lfu_table.get(key, 0) + 1

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if not key or key not in self.cache_data:
            return
        self.lfu_table[key] += 1
        return self.cache_data.get(key)
