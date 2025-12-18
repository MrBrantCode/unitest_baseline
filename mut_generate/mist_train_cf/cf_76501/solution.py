"""
QUESTION:
Create a function named `count_frequency` that takes a list of integers `lst` and a specific number `num` as input. The function should return the frequency of `num` in `lst`. The list `lst` contains integers ranging from 1 to 20. The function should be able to handle cases where `num` is not present in `lst`.
"""

def count_frequency(lst, num):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq.get(num, 0)