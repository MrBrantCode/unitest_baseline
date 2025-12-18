"""
QUESTION:
Write a function called `capitalize_and_reverse` that takes a sentence as input and returns the sentence with all words capitalized and in reverse order. The function should have a time complexity of O(n), where n is the number of words in the sentence, and a space complexity of O(1), meaning it should not use any additional data structures or variables that scale with the input size.
"""

def capitalize_and_reverse(sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Reverse the order of the words and capitalize each word
    reversed_sentence = ' '.join(word.capitalize() for word in reversed(words))

    return reversed_sentence