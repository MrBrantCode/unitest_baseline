"""
QUESTION:
Write a function `reverse_list` that takes a list `lst` as input and reverses its order in place without using the built-in `reverse` function or any additional list or array for temporary storage. The function should return the reversed list.
"""

def reverse_list(lst):
    # Initialize two pointers
    left = 0
    right = len(lst) - 1
    
    # Swap elements until the pointers meet
    while left < right:
        # Swap the elements at left and right indices
        lst[left], lst[right] = lst[right], lst[left]
        
        # Move the pointers towards the center
        left += 1
        right -= 1
    
    return lst