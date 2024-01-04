#!/usr/bin/env python3
"""
LRU caching: LRUCache class
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines:
    - put: adds to lru cache
    - get: get item from lru cache
    """
    def __init__(self):
        super().__init__()
        self.lru_table = OrderedDict()

    def put(self, key, item):
        """
        adds item to lru cache
        """
        if key and item:
            self.lru_table[key] = item
            self.lru_table.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.lru_table))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.lru_table) > BaseCaching.MAX_ITEMS:
            self.lru_table.popitem(last=False)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.lru_table.move_to_end(key)
            return self.cache_data[key]
        return None
