"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input, sets its value to "hello world", reverses the string in-place without using any additional memory, and returns the reversed string. The function should not use any additional memory and should reverse the string using the two-pointer technique.
"""

def entance(s):
    # Set the value of the variable as "hello world"
    s = "hello world"

    # Convert the string to a list
    s_list = list(s)

    # Initialize two pointers
    left = 0
    right = len(s_list) - 1

    # Reverse the string in-place using two pointers
    while left < right:
        # Swap the characters
        s_list[left], s_list[right] = s_list[right], s_list[left]
        
        # Move the pointers towards the center
        left += 1
        right -= 1
    
    # Convert the list back to a string
    s = ''.join(s_list)

    return s