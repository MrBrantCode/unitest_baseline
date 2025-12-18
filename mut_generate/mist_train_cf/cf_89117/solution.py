"""
QUESTION:
Create a function `find_duplicates` that takes an array of elements (which can be negative numbers and floating-point numbers) with a maximum length of 10^9 elements and returns the frequency of each duplicate element. The function should achieve an average time complexity of O(n log n) and space complexity of O(n), where n is the length of the input array.
"""

from collections import defaultdict

def find_duplicates(arr):
    hash_table = defaultdict(int)
    for element in arr:
        hash_table[element] += 1
    result = {element: frequency for element, frequency in hash_table.items() if frequency > 1}
    return result