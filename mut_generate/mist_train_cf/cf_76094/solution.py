"""
QUESTION:
Write a function `analyse_dict` that takes a dictionary `d` as input and returns a tuple containing the total sum of integers, the total number of words in strings, and the total sum of list elements. The function should recursively traverse the dictionary and handle nested dictionaries, integers, strings, and lists. The function should ignore non-integer, non-string, and non-list values.
"""

def analyse_dict(d):
    total_sum = 0
    total_words = 0
    total_list_sum = 0

    for value in d.values():
        if type(value) is int:
            total_sum += value
        elif type(value) is str:
            total_words += len(value.split())
        elif type(value) is list:
            total_list_sum += sum(value)
        elif type(value) is dict:
            dict_sum, dict_words, dict_list_sum = analyse_dict(value)
            total_sum += dict_sum
            total_words += dict_words
            total_list_sum += dict_list_sum

    return total_sum, total_words, total_list_sum