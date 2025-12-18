"""
QUESTION:
Write a function `reverse_list` that takes a list of at least one element as input and reverses its order in-place without using any built-in functions, methods, additional data structures, or recursion. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def reverse_list(input_list):
    left = 0
    right = len(input_list) - 1
    
    while left < right:
        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1
        right -= 1
    
    return input_list