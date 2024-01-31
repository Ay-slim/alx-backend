"""Basic cache 0 module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache - Basic cache class inheriting from BaseCaching
    """
    def put(self, key, item):
        """Put value that sets key and item on parent dict"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Fetch the value associated with given key in parent cache data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
