"""
QUESTION:
Given a string `text`, use its characters to form as many instances of the word "sandwich" as possible, with each character used at most once. The function `maxSandwiches(text)` should return the maximum number of instances that can be formed. The length of `text` is between 1 and 10^4, and it consists of only lower case English letters.
"""

from collections import Counter

def max_sandwiches(text):
    c = Counter(text)
    return min(c[i] // Counter('sandwich')[i] for i in 'sandwich')