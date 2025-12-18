"""
QUESTION:
Implement a recursive function `find_longest_word` that takes a string of words as input and returns the longest word that does not contain the letter "e". If no such word exists, return an empty string. The input string contains only spaces as word separators and does not contain punctuation or special characters.
"""

def find_longest_word(sentence):
    def recursive_find_longest_word(words, longest_word, longest_length):
        if len(words) == 0:
            return longest_word

        if len(words[0]) > longest_length and "e" not in words[0]:
            return recursive_find_longest_word(words[1:], words[0], len(words[0]))

        return recursive_find_longest_word(words[1:], longest_word, longest_length)

    return recursive_find_longest_word(sentence.split(), "", 0)