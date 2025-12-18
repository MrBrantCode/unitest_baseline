"""
QUESTION:
Implement a `CacheMode` class that supports two caching modes: "LRU" (Least Recently Used) and "LFU" (Least Frequently Used). The class should have the following methods: `__init__(self, mode: str)`, `put(self, key: int, value: int)`, and `get(self, key: int) -> int`. The cache should be able to store key-value pairs and evict items based on the specified caching mode. Assume a fixed cache capacity for the implementation. The `put` method should evict the least recently used or least frequently used item if the cache is full, and the `get` method should return the value associated with the given key or -1 if the key does not exist.
"""

from collections import OrderedDict, defaultdict

def cacheMode(mode: str, capacity: int):
    class CacheMode:
        def __init__(self):
            self.mode = mode
            self.capacity = capacity
            self.cache = OrderedDict()
            self.frequency = defaultdict(int)

        def put(self, key: int, value: int):
            if key in self.cache:
                del self.cache[key]
            elif len(self.cache) >= self.capacity:
                if self.mode == "LRU":
                    self.cache.popitem(last=False)
                elif self.mode == "LFU":
                    min_freq_key = min(self.frequency, key=self.frequency.get)
                    del self.cache[min_freq_key]
                    del self.frequency[min_freq_key]

            self.cache[key] = value
            self.frequency[key] += 1

        def get(self, key: int) -> int:
            if key in self.cache:
                self.frequency[key] += 1
                return self.cache[key]
            return -1
    return CacheMode()