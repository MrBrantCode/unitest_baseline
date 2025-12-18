"""
QUESTION:
Write a function named `countSubstring` that takes in an array of strings and a target string, and returns the number of times the target string appears as a substring in the array elements. The target string is a non-empty string of lowercase alphabets with a length between 1 and 100. The function should handle arrays with duplicate elements efficiently and have a time complexity of O(n), where n is the length of the array.
"""

def countSubstring(array, target):
    count = 0
    for string in array:
        count += string.count(target)
    return count