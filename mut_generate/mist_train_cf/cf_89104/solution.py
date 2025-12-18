"""
QUESTION:
Implement a function named `reverse_string` that takes a string variable `s` as input and reverses it in place without using any built-in string manipulation functions or libraries. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), meaning no additional data structures can be used except for the given string variable. The function should also print the reversed string and modify the original string variable to contain the reversed string.
"""

def reverse_string(s):
    # Convert the string to a list of characters
    s = list(s)
    
    # Initialize two pointers
    left = 0
    right = len(s) - 1
    
    # Reverse the string in place
    while left < right:
        # Swap characters at the two pointers
        s[left], s[right] = s[right], s[left]
        
        # Move the pointers towards each other
        left += 1
        right -= 1
    
    # Convert the list of characters back to a string
    s = ''.join(s)
    
    # Print the reversed string
    print(s)
    return s