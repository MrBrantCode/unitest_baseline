"""
QUESTION:
Create a function named `search_keyword` that takes two arguments, `string` and `keyword`, and returns a list of indices where the keyword appears in the string. The search should be case insensitive and return all occurrences of the keyword.
"""

def search_keyword(string, keyword):
    indices = []
    lower_string = string.lower()
    lower_keyword = keyword.lower()
    start_index = lower_string.find(lower_keyword)
    while start_index != -1:
        indices.append(start_index)
        start_index = lower_string.find(lower_keyword, start_index + 1)
    return indices