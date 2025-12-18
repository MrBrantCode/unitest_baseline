"""
QUESTION:
Write a function `sum_to_hex` that calculates the sum of all positive elements in a given array and returns the result as a hexadecimal number. The input array can contain up to 1 million elements, each ranging from -1000 to 1000. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def sum_to_hex(input_array):
    total = 0
    for num in input_array:
        if num > 0:
            total += num
    return hex(total)