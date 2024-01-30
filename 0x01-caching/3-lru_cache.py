#!/usr/bin/env python3
"""3-lru_cache"""
from datetime import datetime

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Cache for LRUCache"""

    def __init__(self,):
        """Initialize LRUCache"""
        super().__init__()
        self._data_info = {}

    def put(self, key, item):
        """Put an item into cache with given key"""
        if key and item:
            if len(self._data_info) >= self.MAX_ITEMS and self.cache_data.get(
                    key) is None:

                lru_value = min(self._data_info.values())
                lru_key = list(self._data_info.keys())[list(
                    self._data_info.values()).index(lru_value)]

                try:
                    del self.cache_data[lru_key]
                    del self._data_info[lru_key]
                    print("DISCARD: " + lru_key)
                except KeyError:
                    pass

            self.cache_data[key] = item
            self._data_info[key] = datetime.now()

    def get(self, key):
        """Returns value with the associated key"""
        if self.cache_data.get(key):
            self._data_info[key] = datetime.now()
            return self.cache_data[key]
