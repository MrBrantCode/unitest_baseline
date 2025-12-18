"""
QUESTION:
Develop a function called `find_mode_and_median` that takes a list of numbers as input and returns a tuple containing a list of modes and the median. The mode is defined as the number(s) that appear most frequently in the list, while the median is the middle number when the numbers are sorted in ascending order. If the list has an even length, the median is the average of the two middle numbers. The function should be able to handle lists of any length.
"""

from collections import Counter

def find_mode_and_median(numbers):
    counter = Counter(numbers)
    max_count = max(counter.values())
    mode = [k for k, v in counter.items() if v == max_count]
    
    n = len(numbers)
    s = sorted(numbers)
    median = (s[n//2] + s[(n - 1) // 2]) / 2
    
    return mode, median