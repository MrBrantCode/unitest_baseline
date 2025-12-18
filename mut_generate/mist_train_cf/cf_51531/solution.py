"""
QUESTION:
Create a function named `sort_array` that takes a list of non-negative integers as input and returns the sorted list. The sorting order is based on the count of '1's in the binary representation of each number in ascending order. If two numbers have the same count of '1's, the sorting order is based on whether the count is odd or even (even first), and if there is still a tie, the sorting order is based on the decimal values.
"""

def sort_array(arr):
    # Define the key function
    def key_func(n):
        # Convert the number to binary and count the '1's
        count = bin(n).count('1')
        # Return a tuple of the count of ones, the parity of the count and the number itself
        return (count, count % 2 == 0, n)

    # Sort the array with the custom key function
    return sorted(arr, key=key_func)