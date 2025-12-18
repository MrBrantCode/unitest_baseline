"""
QUESTION:
Find the missing number from 1 to 100 in an array that may contain duplicates. The function should be named find_missing_element and take a list of integers as input. The function should return the missing number. The time complexity of the function should be O(n), where n is the length of the input array.
"""

def find_missing_element(arr):
    missing = 0
    for i, num in enumerate(arr):
        missing ^= num
        missing ^= i + 1
    for i in range(len(arr), 101):
        missing ^= i + 1
    return missing