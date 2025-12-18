"""
QUESTION:
Write a function `reposition_nums_and_count_unique` that takes a string `s` as input and returns a tuple containing a string with all numerical values repositioned to the end while preserving the order of non-numeric characters, and the count of unique numerical values.
"""

def reposition_nums_and_count_unique(s):
    num_list = []
    num_count = set()
    result_str = ""
    for char in s:
        if char.isdigit():
            num_list.append(char)
            num_count.add(char)
        else:
            result_str += char
    return result_str + ''.join(num_list), len(num_count)