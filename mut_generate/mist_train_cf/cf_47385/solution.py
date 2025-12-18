"""
QUESTION:
Write a function named `frequencySort` that takes a string `s` as input and returns a string sorted in decreasing order based on the frequency of characters. If two characters have the same frequency, maintain their original order in the string. The function should treat characters with different casing as unique characters.
"""

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

def frequencySort(s: str) -> str:
    count = OrderedCounter(s)
    return ''.join(char * freq for char, freq in count.most_common())