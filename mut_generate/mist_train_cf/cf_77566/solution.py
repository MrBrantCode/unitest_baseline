"""
QUESTION:
Construct a Python function named `get_most_common_keys` that takes a nested dictionary `d` as input and returns the key(s) that appears most frequently in total across all nested dictionaries. If a tie occurs, the function should return all the keys with the highest frequency. The function should be capable of handling varying depths of nesting.
"""

from collections import Counter

def get_most_common_keys(d):
    counter = Counter()

    def find_freq_keys(sub_dict):
        for key, value in sub_dict.items():
            counter[key] += 1
            if isinstance(value, dict):
                find_freq_keys(value)

    find_freq_keys(d)
    mc = counter.most_common()
    return [k for k, v in mc if v == mc[0][1]]