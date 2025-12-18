"""
QUESTION:
Create a function called `reverse_array` that takes an array as input and reverses it in place using slicing with a time complexity of O(n). Do not use any built-in functions or libraries that directly reverse the array. The function should modify the input array and return the reversed array.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr