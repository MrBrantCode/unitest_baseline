"""
QUESTION:
Write a function called `countOccurrences` that takes two arguments: an array of integers and a target number. The function should return the number of times the target number appears in the array, considering only the numbers that are greater than or equal to zero. The time complexity of the implementation should be O(n), where n is the length of the array.
"""

def countOccurrences(arr, num):
    count = 0
    for n in arr:
        if n >= 0 and n == num:
            count += 1
    return count