#!/usr/bin/env python3
"""4-mru_cache"""
from datetime import datetime

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Cache for MRUCache"""

    def __init__(self,):
        """Initialize MRUCache"""
        super().__init__()
        self._data_info = {}

    def put(self, key, item):
        """Put an item into cache with given key"""
        if key and item:
            if len(self._data_info) >= self.MAX_ITEMS and self.cache_data.get(
                    key) is None:

                mru_value = max(self._data_info.values())
                mru_key = list(self._data_info.keys())[list(
                    self._data_info.values()).index(mru_value)]

                try:
                    del self.cache_data[mru_key]
                    del self._data_info[mru_key]
                    print("DISCARD: " + mru_key)
                except KeyError:
                    pass

            self.cache_data[key] = item
            self._data_info[key] = datetime.now()

    def get(self, key):
        """Returns value with the associated key"""
        if self.cache_data.get(key):
            self._data_info[key] = datetime.now()
            return self.cache_data[key]
