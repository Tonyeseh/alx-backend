#!/usr/bin/env python3
"""2-lifo_cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """Initializes"""
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """Add a key/value pair to the cache"""
        if key and item:
            if len(self._keys) < self.MAX_ITEMS or key in self._keys:
                self._keys.append(key)
                self.cache_data[key] = item
            else:
                del_key = self._keys.pop(len(self._keys) - 1)
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
