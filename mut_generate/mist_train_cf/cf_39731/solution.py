"""
QUESTION:
Implement the `get_original_value` method in the `MappingCache` class, which takes a mapped value as an argument and returns the original value from `base` that corresponds to the given mapped value. The method should first check if the mapped value is already in the `_mapping_cache` dictionary. If it is, return the corresponding original value. If not, iterate through the remaining values in the `base` sequence, updating the `_mapping_cache` dictionary as it goes, and return the original value when the mapped value is found. If the mapped value is not found in the cache or the iterator, return `None`. The `get_original_value` method should be implemented without modifying the existing attributes and methods of the `MappingCache` class, which includes `base`, `map`, and `_mapping_cache`.
"""

def get_original_value(self, mapped_value):
    if mapped_value in self._mapping_cache:
        return self._mapping_cache[mapped_value]

    for original_value in self._cache_iterator:
        original_mapped_value = self.map(original_value)
        self._mapping_cache[original_mapped_value] = original_value
        if mapped_value == original_mapped_value:
            return original_value

    return None