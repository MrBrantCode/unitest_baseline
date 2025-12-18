"""
QUESTION:
Write a function `reverse_swap_case(sentence)` that takes a string as input, reverses its order, and swaps the case of each letter. The function should work with sentences containing digits, spaces, and special characters, leaving these characters unchanged.
"""

def reverse_swap_case(sentence):
    # Reverse the sentence
    reversed_sentence = sentence[::-1]

    # Swap the case of each letter and return
    return reversed_sentence.swapcase()