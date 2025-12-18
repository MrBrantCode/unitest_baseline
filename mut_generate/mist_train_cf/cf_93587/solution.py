"""
QUESTION:
Write a function named "removeDuplicates" that takes a string "s" as input and returns a string with all duplicate characters removed. The function should only keep the first occurrence of each character. The input string can have a maximum length of 10^6 characters and can contain any ASCII characters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def removeDuplicates(s):
    # Create an empty set to keep track of encountered characters
    encountered = set()
    result = ''
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character has already been encountered
        if char not in encountered:
            # If not, append it to the result string
            result += char
            # Add the character to the encountered set
            encountered.add(char)
    
    # Return the resulting string
    return result