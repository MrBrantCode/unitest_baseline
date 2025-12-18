"""
QUESTION:
Write a function `count_reverse_pairs` that takes a list of strings as input. The function should return the number of unique pairs of strings that are reverses of each other, ignoring case sensitivity, special characters, numerals, and spaces. Each pair should be counted only once, even if the list contains duplicate strings.
"""

def count_reverse_pairs(lst):
    count = 0
    map = {}
    for string in lst:
        cleaned_string = ''.join(e for e in string if e.isalpha()).lower().replace(" ", "")
        reversed_string = cleaned_string[::-1]
        if reversed_string in map:
            if map[reversed_string] == 0:
                count += 1
                map[cleaned_string] = 1
        else:
            map[reversed_string] = 0

    return count