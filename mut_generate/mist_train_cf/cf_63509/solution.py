"""
QUESTION:
Construct a function named `top_n_frequent_keys` that takes two parameters: a dictionary and an integer `n`. The function should return a dictionary containing the top `n` keys with the highest frequency in the input dictionary. If multiple keys have the same highest frequency, they should be returned in lexicographical (alphabetical) order. The returned dictionary should have the key from the input dictionary as the key and its frequency as the value.
"""

from collections import Counter
import operator

def top_n_frequent_keys(dictionary, n):
    counter = Counter(dictionary)
    counter_sorted_by_value = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
    counter_sorted_by_key = sorted(counter_sorted_by_value, key=operator.itemgetter(0))
    counter_sorted_by_key_value = sorted(counter_sorted_by_key, key=operator.itemgetter(1), reverse=True)
    return dict(counter_sorted_by_key_value[:n])