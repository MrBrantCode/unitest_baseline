"""
QUESTION:
Write a function named `invert_string_words` that takes a string as input, reverses the order of each word in the string, and removes the middle character from words with an even number of characters. The input string contains words separated by spaces.
"""

def invert_string_words(string):
    words = string.split()
    inverted_words = []

    for word in words:
        if len(word) % 2 == 0:
            middle_index = len(word) // 2
            inverted_word = word[:middle_index] + word[middle_index+1:][::-1]
        else:
            inverted_word = word[::-1]  

        inverted_words.append(inverted_word)

    inverted_string = " ".join(inverted_words)
    return inverted_string