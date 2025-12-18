"""
QUESTION:
Create a function named `sort_by_binary_len_and_sum` that takes an array of positive integers as input. The function must sort the array based on the length of the binary representation of each integer from smallest to largest, and then by decimal value for integers with the same binary length. Additionally, the function must return the sum of all binary lengths.
"""

def sort_by_binary_len_and_sum(arr):
    arr.sort(key=lambda x: (len(bin(x))-2, x))
    total_bin_len = sum([len(bin(x))-2 for x in arr])
    return (arr, total_bin_len)