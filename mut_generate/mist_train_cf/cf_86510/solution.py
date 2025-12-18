"""
QUESTION:
Write a function called `second_most_frequent` that takes an array as input and returns the second most frequent element, ignoring any duplicates. The array will always contain at least 3 elements.
"""

from collections import Counter

def second_most_frequent(arr):
    # Count the frequency of each element
    counter = Counter(arr)

    # Remove duplicates from the array
    unique_arr = list(set(arr))

    # Sort the unique elements by their frequency in descending order
    sorted_unique_arr = sorted(unique_arr, key=lambda x: counter[x], reverse=True)

    # Return the second most frequent element
    return sorted_unique_arr[1]