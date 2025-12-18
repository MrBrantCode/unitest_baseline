"""
QUESTION:
Create a function `find_substrings` that takes a list of strings `string_list` and a string `sub_string` as inputs, and returns all the strings in the list that contain the given string. The function should handle case sensitivity by recognizing the substring regardless of case, and should return a custom message 'No matches found' if no matches are found.
"""

def find_substrings(string_list, sub_string):
    matched_words = []
    for word in string_list:
        if word.lower().find(sub_string.lower()) != -1:
            matched_words.append(word)
    if not matched_words:
        return 'No matches found.'
    return matched_words