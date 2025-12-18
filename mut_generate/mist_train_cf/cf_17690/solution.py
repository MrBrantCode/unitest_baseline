"""
QUESTION:
Create a function named `reverse_list` that takes a list of at least one element as input and reverses the order of its elements without using any built-in functions or methods, additional data structures, or recursion. The solution should have a time complexity of O(n) and a space complexity of O(1). The function should return the reversed list.
"""

def reverse_list(input_list):
    left = 0
    right = len(input_list) - 1
    
    while left < right:
        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1
        right -= 1
    
    return input_list