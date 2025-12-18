"""
QUESTION:
Write a function named `find_most_frequent_value` that takes a list of integers and non-integer values as input and returns the value that appears most frequently in the list. The list will always contain at least one repeated value. The function should have a time complexity of O(n), where n is the number of elements in the list.
"""

def find_most_frequent_value(nums):
    frequency = {}
    
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    most_frequent_value = max(frequency, key=lambda x: frequency[x])
    return most_frequent_value