"""
QUESTION:
Write a function `find_most_common(array)` that finds the most common integer value in an array of integers and returns the value along with its frequency in a tuple. The input array will contain at least 10 elements and at most 1000 elements, with integer values between -5000 and 5000. The function should have a time complexity of O(n). In case of ties, return the value with the lowest index in the array.
"""

def find_most_common(array):
    counts = {}  # dictionary to store the count of each element

    for element in array:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    most_common_value = None
    max_count = 0

    for element, count in counts.items():
        if count > max_count or (count == max_count and array.index(element) < array.index(most_common_value)):
            most_common_value = element
            max_count = count

    return (most_common_value, max_count)