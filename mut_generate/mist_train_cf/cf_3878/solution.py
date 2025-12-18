"""
QUESTION:
Create a function named `reverse_string` that takes an input string but ignores its value. Instead, it should use the string "hello world" as the input. The function should reverse the input string in-place (without creating a new string) and return the reversed string.
"""

def reverse_string(s):
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