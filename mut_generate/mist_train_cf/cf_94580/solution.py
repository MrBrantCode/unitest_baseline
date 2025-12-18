"""
QUESTION:
Write a function `find_most_frequent` that takes an array of integers as input and returns the most frequent element in the array. The function must have a time complexity of O(n) and cannot use any built-in functions or data structures like max(), sorted(), Counter, or defaultdict. The input array can contain up to 1 million elements.
"""

def find_most_frequent(arr):
    # Create an empty dictionary to store the frequency count of elements
    freq_count = {}

    # Iterate through the array
    for num in arr:
        # If the element is already in the dictionary, increment its count by 1
        if num in freq_count:
            freq_count[num] += 1
        # Otherwise, add the element to the dictionary with a count of 1
        else:
            freq_count[num] = 1

    # Find the element with the maximum count
    most_frequent_element = None
    max_count = 0
    for num, count in freq_count.items():
        if count > max_count:
            max_count = count
            most_frequent_element = num

    return most_frequent_element