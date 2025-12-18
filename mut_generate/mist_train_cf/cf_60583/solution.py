"""
QUESTION:
Write a function named `replace_words` that takes a base string and a dictionary of replacements as input, and returns the modified string where all occurrences of the keys in the dictionary are replaced with their corresponding values, without using any built-in replace functions. The function should split the base string into words, replace the words using the dictionary, and join the words back into a string.
"""

def replace_words(base_string, replacements):
    # split the base string into words
    base_words = base_string.split()

    # replace words using the replacements dictionary
    result_words = [replacements.get(word, word) for word in base_words]

    # join new words into a string
    output_string = ' '.join(result_words)

    return output_string