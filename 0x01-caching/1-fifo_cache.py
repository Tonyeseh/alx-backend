#!/usr/bin/env python3
"""1-fifo_cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self,):
        """Initialize"""
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """Put a key/value pair to the cache."""
        if key and item:
            if len(self._keys) < self.MAX_ITEMS or key in self._keys:
                self._keys.append(key)
                self.cache_data[key] = item
            else:
                del_key = self._keys.pop(0)
                try:
                    del self.cache_data[del_key]
                    print("DISCARD: {}".format(del_key))
                except KeyError:
                    pass
                self.cache_data[key] = item
                self._keys.append(key)

    def get(self, key):
        """Returns the value associated with key or None"""
        if key:
            return self.cache_data.get(key)
