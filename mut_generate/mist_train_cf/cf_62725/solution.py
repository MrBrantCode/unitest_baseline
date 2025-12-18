"""
QUESTION:
Write a function `split_words` that takes a string of words as input and returns a list of words separated by either whitespace or commas. If the input string does not contain any whitespace or commas, return the count of lower-case alphabetic characters with an odd index (where 'a' has an index of 0, 'b' has an index of 1, ..., and 'z' has an index of 25) in the string.
"""

def split_words(txt):
    import re

    word_list = re.split(",| ", txt)
    if len(word_list) == 1:
        count = 0
        for char in txt:
            if char.islower() and (ord(char) - ord("a")) % 2 == 1:
                count += 1
        return count
    return word_list