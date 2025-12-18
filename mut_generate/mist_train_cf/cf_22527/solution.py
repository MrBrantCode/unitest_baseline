"""
QUESTION:
Create a function `check_strings` that takes an array of strings as input and returns a list of strings with a length of exactly 5. The resulting list should be sorted in descending order based on the sum of the ASCII values of the characters in each string.
"""

def check_strings(arr):
    # Initialize an empty list to store the valid strings
    valid_strings = []
    
    # Iterate over each string in the array
    for string in arr:
        # Check if the length of the string is exactly 5
        if len(string) == 5:
            # Calculate the sum of ASCII values of characters in the string
            ascii_sum = sum(ord(c) for c in string)
            
            # Append the string and its ASCII sum as a tuple to the valid_strings list
            valid_strings.append((string, ascii_sum))
    
    # Sort the valid_strings list in descending order based on the ASCII sum
    valid_strings.sort(key=lambda x: x[1], reverse=True)
    
    # Return a list of the strings from the sorted valid_strings list
    return [string for string, _ in valid_strings]