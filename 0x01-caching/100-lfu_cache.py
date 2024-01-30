#!/usr/bin/env python3
"""100-lfu_cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache Class"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self._data_info = {}

    def put(self, key, item):
        """sets the key to value in the cache"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS and self.cache_data.get(key) is None:
                del_val = min(self._data_info.values())
                del_key = list(self._data_info.keys())[list(self._data_info.values()).index(del_val)]

                try:
                    del self.cache_data[del_key]
                    del self._data_info[del_key]
                    print("DISCARD: " + del_key)

                except KeyError:
                    pass

            self.cache_data[key] = item
            self._data_info[key] = self._data_info.get(key, 0) + 1

    def get(self, key):
        """gets the key from the cache"""
        if key and self.cache_data.get(key):
            self._data_info[key] = self._data_info.get(key, 0) + 1
            return self.cache_data[key]