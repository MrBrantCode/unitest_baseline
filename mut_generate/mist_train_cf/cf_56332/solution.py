"""
QUESTION:
Create a function named `count_char` that takes a string as input and returns a dictionary containing the frequency of each character in the string. The function should handle capital letters as distinct characters from their lowercase counterparts and include special characters and whitespaces in the count. The dictionary should be sorted by the characters' frequency in descending order.
"""

from collections import Counter, OrderedDict

def count_char(string):
    count = Counter(string)
    count = OrderedDict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    return count