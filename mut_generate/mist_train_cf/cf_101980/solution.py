"""
QUESTION:
Write a function called `get_third_character` that takes a string `word` as input, removes any leading or trailing whitespace characters, and returns the third character of the resulting string. The function should only use a single loop iteration and no built-in functions other than those required for basic operations (e.g., string iteration, comparison). The input string is guaranteed to have at least three characters.
"""

def get_third_character(word):
    # Remove leading and trailing whitespace characters
    word = word.strip()

    # Initialize a counter variable
    count = 0

    # Iterate through each character in the word
    for char in word:
        # Increment the counter
        count += 1

        # Check if we have reached the third character
        if count == 3:
            # Return the third character
            return char