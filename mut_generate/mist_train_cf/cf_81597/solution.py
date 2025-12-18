"""
QUESTION:
Construct a function `sort_by_binary_len` that takes an array of non-negative integers and returns the array sorted by the length of their binary representations in ascending order. If multiple numbers have the same binary length, they should be sorted by their decimal values in ascending order.
"""

def sort_by_binary_len(arr):
    # Calculate the binary length of each number
    # Add it as a tuple with a number in a new array
    binary_len_arr = [(num, len(bin(num)[2:])) for num in arr]
    # Sort the new array based on the second element of each tuple,
    # which is the binary length, and in case of equality
    # python's sort is a stable sort that maintains relative order,
    # thus multiple numbers with same binary length will be sorted 
    # in the order of their original appearances in arr.
    binary_len_arr.sort(key=lambda x: (x[1], x[0]))
    # Return only the numbers
    return [num for num, _ in binary_len_arr]