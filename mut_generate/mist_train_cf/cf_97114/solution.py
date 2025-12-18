"""
QUESTION:
Create a function named `is_pangram` that takes a string `s` as input. The function should check if `s` is a pangram (contains all the letters of the alphabet at least once) and return a boolean value indicating whether it's a pangram along with a dictionary containing the count of each letter in the pangram. The function must have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), meaning it should use a constant amount of space regardless of the input size.
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