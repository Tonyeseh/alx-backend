#!/usr/bin/env python3
"""0-basic_cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic cache class"""

    def __init__(self,):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Put a key/value pair into the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get a key/value pair from the cache"""
        return self.cache_data.get(key)
