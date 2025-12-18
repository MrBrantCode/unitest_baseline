"""
QUESTION:
Create a function named `replace_last_occurrence` that takes two parameters: `string` and `word`. The function should replace the last occurrence of `word` in `string` with the capitalized version of `word`, but only if the last occurrence is not part of another word and is immediately followed by a comma. The replacement should be case-insensitive, and the original capitalization of the word in the replaced string should be maintained.
"""

def replace_last_occurrence(string, word):
    words = string.split()
    last_index = -1
    capitalized_word = word.capitalize()

    for i in range(len(words)-1, -1, -1):
        if words[i].lower() == word.lower() and (i == len(words) - 1 or words[i+1] == ","):
            words[i] = words[i].capitalize()
            last_index = i
            break

    if last_index != -1:
        return " ".join(words)
    return string