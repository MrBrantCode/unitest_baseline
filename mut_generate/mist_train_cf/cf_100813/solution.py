"""
QUESTION:
Create a function called `reverse_words` that takes a string as input and returns a table. The table should contain the reversed order of each word in the string (excluding any words that are less than 3 characters in length) along with the number of characters in each word.
"""

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        if len(word) >= 3:
            reversed_words.append((word[::-1], len(word)))
    table = "\n".join([f"{word[0]:<10}{word[1]}" for word in reversed_words])
    return table