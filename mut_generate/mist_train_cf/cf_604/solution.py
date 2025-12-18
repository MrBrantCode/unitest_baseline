"""
QUESTION:
Develop a function `second_most_frequent` that takes an array as input, and returns the second most frequent unique element in the array. The input array contains at least 3 elements. The function should return the element itself, not its frequency, and the array may contain duplicates.
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