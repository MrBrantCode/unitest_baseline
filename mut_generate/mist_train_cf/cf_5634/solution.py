"""
QUESTION:
Write a function named `countSubstring` that takes in an array of strings and a non-empty target string, and returns the number of times the target string appears as a substring in the array elements. The function should be able to handle an array of up to 10^6 elements and have a time complexity of O(n), where n is the length of the array.
"""

def countSubstring(array, target):
    count = 0
    for string in array:
        count += string.count(target)
    return count