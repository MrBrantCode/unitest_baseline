"""
QUESTION:
Write a function `rearrange_spaces` that takes a string `text` of words separated by spaces and returns the string after rearranging the spaces so that there is an equal number of spaces between every pair of adjacent words, and the number of spaces between the words and the number of extra spaces at the end. If the spaces cannot be evenly distributed, the extra spaces should be placed at the end of the string. The length of the returned string should be the same as the original string. The function should handle cases where the input string contains at least one word and is composed of lowercase English letters and spaces.
"""

def rearrange_spaces(text):
    words = text.split()
    count_of_spaces = text.count(' ')

    if len(words) == 1:
        return words[0] + ' ' * count_of_spaces

    space_between_words, extra_spaces = divmod(count_of_spaces, len(words) - 1)
    return (' ' * space_between_words).join(words) + ' ' * extra_spaces