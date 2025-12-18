"""
QUESTION:
Write a function `sum_to_hex` that takes an array of up to 1 million integers, each ranging from -1000 to 1000, as input and returns the sum of all positive elements in the array as a hexadecimal string. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def sum_to_hex(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return hex(total)