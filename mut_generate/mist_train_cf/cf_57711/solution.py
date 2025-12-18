"""
QUESTION:
Write a function named `longest_word(s)` that takes a string `s` as input, splits it into words, and identifies the longest words, returning them as a list. If there are multiple words of the same maximum length, return all of them.
"""

def longest_word(s):
    s_list = s.split(' ')
    longest_words = [s_list[0]]

    for word in s_list[1:]:
        if len(word) > len(longest_words[0]):
            longest_words = [word]
        elif len(word) == len(longest_words[0]):
            longest_words.append(word)
          
    return longest_words