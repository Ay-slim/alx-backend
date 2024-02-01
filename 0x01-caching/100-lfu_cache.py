"""Lfu cache 1 module"""


from datetime import datetime
from base_caching import BaseCaching


def lfu_helper(access_log):
    """Function to figure out lfu to discard"""
    max_count_tracker = {}
    count_tracker = 0
    for key, val in access_log.items():
        if val['count'] == count_tracker:
            max_count_tracker[key] = val['time']
        if val['count'] > count_tracker:
            max_count_tracker = {key: val['time']}
            count_tracker = val['count']
    return min(max_count_tracker, key=max_count_tracker.get)


class LFUCache(BaseCaching):
    """
    LFUCache - LFU cache class inheriting from BaseCaching
    """
    def __init__(self):
        """Override init"""
        super().__init__()
        self.access_log = {}

    def put(self, key, item):
        """Put value that sets key and item on parent dict"""
        if key and item:
            self.cache_data[key] = item
            self.access_log[key] = {
                'time': datetime.now(),
                'count': 0
            }
            if len(self.cache_data) > self.MAX_ITEMS:
                key_to_discard = lfu_helper(self.access_log)
                self.cache_data.pop(key_to_discard)
                self.access_log.pop(key_to_discard)
                print("DISCARD: {}".format(key_to_discard))

    def get(self, key):
        """Fetch the value associated with given key in parent cache data"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.access_log[key]['time'] = datetime.now()
        self.access_log[key]['count'] += 1
        return self.cache_data[key]
