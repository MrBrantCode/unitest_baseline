"""
QUESTION:
Create a recursive function called `is_reverse_anagram` that determines whether a given word is an anagram when its characters are arranged in reverse order. The function should take a string as input and return a boolean value. The input string is assumed to be lowercase, and may not contain punctuation or spaces.
"""

def is_reverse_anagram(word):
    # Base case: When word is of length 0 or 1, it's a reversal of itself
    if len(word) <= 1:
        return True
    # Recursive case: Compare first and last letters, and then the rest
    else:
        # If the first and last letters are the same
        if word[0] == word[-1]:
            # Call function on the substring that omits the first and last letters
            return is_reverse_anagram(word[1:-1])
        else:
            # If the first and last letters differ, it's not a reverse anagram
            return False