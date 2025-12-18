"""
QUESTION:
Write a function named `count_target` that takes an array of integers and a non-zero target integer as input and returns the number of times the target integer appears in the array. The function should have a time complexity of O(n), where n is the length of the array, and it should be able to handle arrays with a maximum length of 10^6.
"""

def count_target(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count