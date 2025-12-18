"""
QUESTION:
Write a function called `replace_words_with_star` that takes two parameters: `input_string` and `word_list`. The function should replace all occurrences of each word in `word_list` with '*' in `input_string` and return the modified string. The replacement should be case-sensitive and handle multiple occurrences of the words in the string. The function can assume that `input_string` and `word_list` are not empty, and `input_string` has no leading or trailing spaces, but `word_list` may contain leading or trailing spaces.
"""

def replace_words_with_star(input_string, word_list):
    for word in word_list:
        word_to_replace = word.strip()  # remove leading and trailing spaces
        input_string = input_string.replace(word_to_replace, "*")
    return input_string