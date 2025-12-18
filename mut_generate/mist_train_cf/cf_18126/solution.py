"""
QUESTION:
Write a function named `replace_word_a` that takes a string of words as input and returns the string with all occurrences of the word "a" (ignoring case) replaced by "the", preserving the original word order and case.
"""

def replace_word_a(word_string):
    """
    Replaces all occurrences of the word "a" (ignoring case) with "the" in a given string, 
    preserving the original word order and case.

    Args:
        word_string (str): The input string.

    Returns:
        str: The modified string with all occurrences of "a" replaced by "the".
    """
    words = word_string.split()  # Split the string into a list of words

    for i in range(len(words)):
        if words[i].lower() == "a":
            # Preserve the original case of the word
            if words[i].islower():
                words[i] = "the"
            elif words[i].istitle():
                words[i] = "The"
            elif words[i].isupper():
                words[i] = "THE"

    # Join the modified list of words back into a string
    return ' '.join(words)