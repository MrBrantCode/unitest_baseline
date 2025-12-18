"""
QUESTION:
Write a function `is_palindrome(input_string)` that checks if a given input string is a palindrome, ignoring any non-alphanumeric characters and considering it case-insensitive. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def is_palindrome(input_string):
    # Convert the input string to lowercase
    input_string = input_string.lower()
    
    # Initialize pointers to the start and end of the string
    start = 0
    end = len(input_string) - 1
    
    # Loop until the pointers meet or cross each other
    while start < end:
        # Ignore any non-alphanumeric characters from the start of the string
        while not input_string[start].isalnum():
            start += 1
            # Break the loop if the pointers meet or cross each other
            if start >= end:
                break
        
        # Ignore any non-alphanumeric characters from the end of the string
        while not input_string[end].isalnum():
            end -= 1
            # Break the loop if the pointers meet or cross each other
            if start >= end:
                break
        
        # If the characters at the pointers are not equal, return False
        if input_string[start] != input_string[end]:
            return False
        
        # Move the pointers towards each other
        start += 1
        end -= 1
    
    # If the loop completes without returning False, the input is a palindrome
    return True