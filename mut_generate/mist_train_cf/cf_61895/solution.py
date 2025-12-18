"""
QUESTION:
Write a function named `process_string` that takes a string as input, converts it to lowercase, reverses the order of words, and maintains the period at the end of the sentence. The input string is assumed to have words separated by a single space and ends with a period. Use recursion to reverse the order of words.
"""

def process_string(string):
    words = string[:-1].lower().split(' ')
    def recursive_reversal(words):
        if len(words) == 0:
            return []
        else:
            return recursive_reversal(words[1:]) + [words[0]]
    reversed_words = recursive_reversal(words)
    return " ".join(reversed_words) + "."