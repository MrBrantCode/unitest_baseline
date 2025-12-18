"""
QUESTION:
Write a function `reverse_array` that takes an array of integers as input and returns a string with each number in reverse order, separated by a comma. The function must achieve a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array.
"""

def reverse_array(arr):
    # Convert the array to a string, with each number separated by a comma
    arr_string = ','.join(str(x) for x in arr)

    # Reverse the string using slicing
    reversed_string = arr_string[::-1]

    return reversed_string