#!/usr/bin/python3
"""FIFO Cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching System"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_key)
            print('DISCARD: {}'.format(first_key))

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
