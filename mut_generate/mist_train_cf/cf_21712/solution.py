"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` containing only alphabetic characters with a maximum length of 100 as input and reverses it in-place without using any additional data structures or built-in string reverse methods. The function should have a time complexity of O(n), where n is the length of the string, and return the reversed string.
"""

def reverse_string(s):
    # Convert the string into a list of characters
    char_list = list(s)
    
    # Initialize the left and right pointers
    left = 0
    right = len(char_list) - 1
    
    # Reverse the string in-place
    while left < right:
        # Swap the characters at the left and right pointers
        char_list[left], char_list[right] = char_list[right], char_list[left]
        
        # Move the pointers towards each other
        left += 1
        right -= 1
    
    # Convert the list of characters back into a string
    reversed_string = ''.join(char_list)
    
    return reversed_string