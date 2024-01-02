#!/usr/bin/env python3
"""
Basic Dictionary: BasicCache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines:
    - put method: add to cache dictionary
    - get method: get from cache dictionary
    """

    def put(self, key, item):
        """
        adds item to cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        retrieves item from cache
        """
        return self.cache_data.get(key)
