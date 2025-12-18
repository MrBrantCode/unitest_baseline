"""
QUESTION:
Given a list of integers and non-integer values, write a function `find_most_frequent_value` to find the value that appears most frequently. The function should have a time complexity of O(n) and should work for a list with millions of elements. The list may contain negative numbers, non-integer values, and repeated values, and the maximum value of any element is 10^6.
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