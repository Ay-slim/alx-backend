"""Fifo cache 1 module"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache - FIFO cache class inheriting from BaseCaching
    """
    def put(self, key, item):
        """Put value that sets key and item on parent dict"""
        if key and item:
            self.cache_data[key] = item
        cache_keys = list(self.cache_data.keys())
        if len(cache_keys) > self.MAX_ITEMS:
            key_to_discard = cache_keys[0]
            self.cache_data.pop(key_to_discard)
            print("DISCARD: {}".format(key_to_discard))

    def get(self, key):
        """Fetch the value associated with given key in parent cache data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
