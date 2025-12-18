"""
QUESTION:
Write a function called `reverse_array` that takes an array of integers as input and returns a string where each number in the array appears in reverse order, separated by commas. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.
"""

def reverse_array(arr):
    # Convert the array to a string, with each number separated by a comma
    arr_string = ','.join(str(x) for x in arr)

    # Reverse the string using slicing
    reversed_string = arr_string[::-1]

    return reversed_string