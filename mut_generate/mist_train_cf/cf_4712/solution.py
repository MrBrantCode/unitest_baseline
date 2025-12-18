"""
QUESTION:
Write a function named `count_words` that takes a string as input and returns a dictionary where each unique word in the string is a key and the number of times it appears in the string is its value. The function should ignore punctuation marks, treat uppercase and lowercase letters as the same, and handle multiple spaces, tabs, newline characters, or hyphens as word separators. The function should not use any built-in string manipulation libraries and should have a time complexity of O(n), where n is the length of the input string.
"""

def entance(string):
    # Remove punctuation marks and convert to lowercase
    string = string.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('-', '')
    string = string.lower()

    # Split the string into words, handling multiple spaces, tabs, newline characters, or hyphens as word separators
    words = string.replace('  ', ' ').replace('\t', ' ').replace('\n', ' ').split()

    # Initialize an empty dictionary
    word_count = {}

    # Iterate through each word in the list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            word_count[word] = 1

    return word_count