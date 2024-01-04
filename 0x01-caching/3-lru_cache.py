#!/usr/bin/python3
""" 3-lru_cache """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache"""

    def __init__(self):
        """Initialize the LRU Cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
