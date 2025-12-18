"""
QUESTION:
Write a function `find_first_non_duplicate(s)` that finds the first non-duplicate character in a given string `s`. The function should treat uppercase and lowercase letters as the same, and consider special characters and numbers. If no non-duplicate character exists, the function should return `None`.
"""

def find_first_non_duplicate(s):
    # Convert the string to lowercase to consider both uppercase and lowercase letters as the same
    s = s.lower()
    # Create an empty dictionary to store the frequency of each character
    freq = {}
    # Iterate over each character in the string
    for char in s:
        # Increment the frequency of the character by 1 in the dictionary
        freq[char] = freq.get(char, 0) + 1
    # Iterate over each character in the string again
    for char in s:
        # Check if the frequency of the character is 1
        if freq[char] == 1:
            return char
    # If no non-duplicate character is found, return None
    return None