"""
QUESTION:
Write a function called `replace_last_occurrence` that takes two parameters: `string` and `word`. Replace the last occurrence of `word` in `string` with the capitalized version of `word`, but only if the last occurrence of `word` is not part of another word and is immediately followed by a comma. The replacement should be case-insensitive, and the original capitalization of the word in the replaced string should be maintained. If the last occurrence of `word` does not meet these conditions, return the original `string`.
"""

def replace_last_occurrence(string, word):
    # Split the string into words
    words = string.split()

    # Initialize variables to store the index and capitalized version of the word
    last_index = -1
    capitalized_word = word.capitalize()

    # Iterate over the words in reverse order
    for i in range(len(words)-1, -1, -1):
        # If the word is the last occurrence and is followed by a comma, replace it
        if words[i].lower() == word.lower() and (i+1 < len(words) and words[i+1] == ","):
            words[i] = capitalized_word
            last_index = i
            break

    # If the word was found and replaced, join the words back into a string
    if last_index != -1:
        replaced_string = " ".join(words)
        return replaced_string

    # If the word was not found, return the original string
    return string