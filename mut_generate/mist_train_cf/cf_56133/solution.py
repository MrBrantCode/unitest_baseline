"""
QUESTION:
Create a function `extract_and_reverse_a_words` that takes a string `sentence` as input and returns a new string containing every word that commences with the letter 'a' in the given sentence. The extracted words should be in reverse order. The function should be case-insensitive when checking for words starting with 'a'.
"""

def extract_and_reverse_a_words(sentence):
    # break sentence down into words and store them in a list
    words = sentence.split()

    # list comprehension to select words that start with 'a' and store them in a list
    a_words = [word for word in words if word.lower().startswith('a')]

    # reverse the order of words in a_words list
    a_words = a_words[::-1]

    # join words in a_words list to create a new string
    return ' '.join(a_words)