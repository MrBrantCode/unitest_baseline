"""
QUESTION:
Write a function named `remove_duplicates` that takes an array of integers as input and returns a new array with duplicates removed while maintaining the original order. The function should have a time complexity of O(n) and use only constant space. The input array can contain integers ranging from -10^9 to 10^9 and have a maximum length of 10^6.
"""

def remove_duplicates(arr):
    unique_set = set()
    unique_arr = []

    for num in arr:
        if num not in unique_set:
            unique_set.add(num)
            unique_arr.append(num)

    return unique_arr