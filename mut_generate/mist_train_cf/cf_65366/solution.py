"""
QUESTION:
Create a function named 'can_form_palindrome' that determines whether a given string of alphanumeric characters can be rearranged into a palindrome. The function should accept a string as input and return a boolean value indicating whether it can form a palindrome. Note that the function should consider the entire ASCII character set (including uppercase and lowercase letters, numbers, and special characters) and return True if the input string can be rearranged into a palindrome, and False otherwise.
"""

def can_form_palindrome(string):
    # Create a count array to store count of characters
    count_map = [0]*256  # Assuming ASCII characters
 
    # Traverse through given string and increment
    # count of characters in count_map.
    for char in string:
        count_map[ord(char)] += 1
 
    # Count odd occurring characters
    odd_count = 0
    for count in count_map:
        if count % 2 != 0:
            odd_count += 1
    
    # Return true if the count of odd occurrences is less than or equal to 1.
    return odd_count <= 1