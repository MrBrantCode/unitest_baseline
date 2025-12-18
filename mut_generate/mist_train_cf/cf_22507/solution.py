"""
QUESTION:
Construct a function named `is_pangram(s)` that takes a string `s` as input, checks if it's a pangram, and returns a boolean value indicating whether the string is a pangram along with a dictionary containing the count of each letter in the string. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). The function should ignore non-alphabetic characters and be case-insensitive.
"""

def is_pangram(s):
    # Create a dictionary to store the count of each letter
    count = {}

    # Iterate over each character in the string
    for char in s:
        # Ignore non-alphabetic characters
        if not char.isalpha():
            continue

        # Convert the character to lowercase
        char = char.lower()

        # Update the count of the character in the dictionary
        count[char] = count.get(char, 0) + 1

    # Check if the string is a pangram by checking if count has 26 unique letters
    if len(count) == 26:
        return True, count
    else:
        return False, count