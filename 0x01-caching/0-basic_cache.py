#!/usr/bin/python3
"""Basic Cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching System"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
