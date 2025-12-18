"""
QUESTION:
Write a function `find_smallest_positive_integer` that takes a list of integers as input and returns the smallest positive integer that is not present in the list. The input list can contain up to 1,000,000 integers, including both positive and negative numbers, and may be empty. The function should have a time complexity of O(n), where n is the number of unique integers in the list, and a space complexity of O(1), without using any additional data structures or libraries. It should also handle duplicate integers in the input list and ignore them when finding the smallest positive integer, and report any instances of integer overflow that occur during its execution.
"""

def find_smallest_positive_integer(lst):
    if not lst:
        return 1
    
    max_num = max(lst)
    
    if max_num <= 0:
        return 1
    
    bit_vector = 0
    
    for num in lst:
        if num > 0:
            bit_vector |= 1 << (num - 1)
    
    for i in range(max_num):
        if not bit_vector & (1 << i):
            return i + 1
    
    return max_num + 1