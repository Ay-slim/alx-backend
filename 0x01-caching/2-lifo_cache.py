"""Lifo cache 1 module"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache - LIFO cache class inheriting from BaseCaching
    """
    def __init__(self):
        """Override init"""
        super().__init__()
        self.added_similar = None

    def put(self, key, item):
        """Put value that sets key and item on parent dict"""
        if key and item:
            cache_keys = list(self.cache_data.keys())
            if key in cache_keys:
                self.added_similar = key
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                key_to_discard = cache_keys[len(cache_keys) - 1]
                if self.added_similar and key != self.added_similar:
                    key_to_discard = self.added_similar
                    self.added_similar = None
                self.cache_data.pop(key_to_discard)
                print("DISCARD: {}".format(key_to_discard))

    def get(self, key):
        """Fetch the value associated with given key in parent cache data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
