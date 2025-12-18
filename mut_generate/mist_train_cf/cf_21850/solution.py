"""
QUESTION:
Write a function `find_most_common(array)` to find the most common value in an array of integers and return a tuple containing the most common value and its frequency. The array will have between 10 and 1000 elements, with integers ranging from -5000 to 5000. If multiple values have the same maximum frequency, return the one with the lowest index in the array. The function should have a time complexity of O(n).
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