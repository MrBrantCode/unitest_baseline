"""
QUESTION:
Implement the function `reverse_words(sentence)` to reverse the order of words in a given sentence without using any additional data structures or built-in string manipulation functions. The sentence only contains letters and spaces, and the solution should have a time complexity of O(n), where n is the length of the sentence. Additionally, the solution must not use any additional variables to store intermediate values, and all manipulations must be done directly on the input sentence. The input sentence should be treated as a list of characters.
"""

def reverse_words(sentence):
    # Reverse the entire sentence
    sentence = reverse_string(sentence)

    # Reverse each word in the sentence
    start = 0
    end = 0
    while end < len(sentence):
        if sentence[end] == ' ':
            sentence = reverse_string(sentence, start, end-1)
            start = end + 1
        end += 1

    # Reverse the last word in the sentence
    sentence = reverse_string(sentence, start, end-1)

    return sentence

def reverse_string(sentence, start=0, end=None):
    # Helper function to reverse a string or a part of it
    if end is None:
        end = len(sentence) - 1

    while start < end:
        sentence[start], sentence[end] = sentence[end], sentence[start]
        start += 1
        end -= 1

    return sentence