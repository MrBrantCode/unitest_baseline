"""
QUESTION:
Write a function named `count_substrings` that takes two parameters: a string `string` and an integer `k`. The function should return the number of substrings in `string` that contain exactly `k` different alphabetical characters, ignoring any non-alphabetical characters and considering only the alphabetical characters in the string.
"""

def count_substrings(string, k):
    # Remove special characters and numbers from the string
    cleaned_string = ''.join(char for char in string if char.isalpha())
    
    # Initialize a counter to keep track of the number of substrings
    count = 0
    
    # Loop through all possible substrings
    for i in range(len(cleaned_string)):
        for j in range(i+1, len(cleaned_string)+1):
            # Check if the substring has exactly k different characters
            if len(set(cleaned_string[i:j])) == k:
                count += 1
    
    return count