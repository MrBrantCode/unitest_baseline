"""
QUESTION:
Create a function `reverse_array` that takes an array of integers as input and returns a string where each number from the array is in reverse order and separated by commas. The original array should not be modified.
"""

def reverse_array(arr):
    reversed_arr = arr[::-1]  # Reverse the array
    string_arr = [str(num) for num in reversed_arr]  # Convert each number to a string
    return ','.join(string_arr)  # Join the strings with a comma separator