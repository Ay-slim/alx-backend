"""Lifo cache 1 module"""


from datetime import datetime
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache - LRU cache class inheriting from BaseCaching
    """
    def __init__(self):
        """Override init"""
        super().__init__()
        self.access_log = {}

    def put(self, key, item):
        """Put value that sets key and item on parent dict"""
        if key and item:
            self.cache_data[key] = item
            self.access_log[key] = datetime.now()
            if len(self.cache_data) > self.MAX_ITEMS:
                key_to_discard = min(self.access_log, key=self.access_log.get)
                self.cache_data.pop(key_to_discard)
                self.access_log.pop(key_to_discard)
                print("DISCARD: {}".format(key_to_discard))

    def get(self, key):
        """Fetch the value associated with given key in parent cache data"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.access_log[key] = datetime.now()
        return self.cache_data[key]
