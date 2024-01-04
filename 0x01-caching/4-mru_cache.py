#!/usr/bin/env python3
"""
MRU caching: MRUCache class
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines:
    - put: adds to mru cache
    - get: get item from mru cache
    """
    def __init__(self):
        super().__init__()
        self.mru_table = OrderedDict()

    def put(self, key, item):
        """
        adds item to mru cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.mru_table[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.mru_table))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.mru_table) > BaseCaching.MAX_ITEMS:
            self.mru_table.popitem(last=False)

        self.mru_table.move_to_end(key, last=False)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.mru_table.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
