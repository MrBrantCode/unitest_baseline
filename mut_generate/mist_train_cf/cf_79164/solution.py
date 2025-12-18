"""
QUESTION:
Create a function called `find_most_frequent_odd` that finds the most frequent odd number in an array of integers. The function should return the most frequent odd number. If there are no odd numbers in the array, it should return a message indicating that.
"""

from collections import Counter

def find_most_frequent_odd(array):
    counter = Counter(array)
    # get only odd numbers and their counts
    odd_counter = {k: v for k, v in counter.items() if k % 2 != 0}
    if odd_counter:
        # return element with maximum count
        return max(odd_counter, key=odd_counter.get)
    else:
        return "No odd numbers in array"