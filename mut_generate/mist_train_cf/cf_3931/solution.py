"""
QUESTION:
Design a function named `reverse_list` that takes a list as input and reverses the order of its elements in-place, without using any built-in functions or methods for reversing the list. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list. It should be able to handle lists containing duplicate elements and print the reversed list.
"""

def reverse_list(my_list):
    # Swap elements in-place using two pointers
    left = 0
    right = len(my_list) - 1
    
    while left < right:
        my_list[left], my_list[right] = my_list[right], my_list[left]
        left += 1
        right -= 1
    
    # Return the reversed list
    return my_list