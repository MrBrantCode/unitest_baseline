"""
QUESTION:
Write a function called `count_four` that counts the occurrence of the number 4 in a given array without using the built-in count function or any additional data structures. The function should have a time complexity of O(n), where n is the length of the array. The function should take an array as input and return the count of 4 in the array.
"""

def count_four(arr):
    count = 0
    for num in arr:
        if num == 4:
            count += 1
    return count