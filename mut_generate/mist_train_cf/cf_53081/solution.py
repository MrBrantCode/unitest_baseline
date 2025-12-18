"""
QUESTION:
Create a function named `solve_string_problem` that takes two strings as input. The function should compare the lengths of the two strings and return the longer string, as well as a dictionary containing the frequency of each unique character in the longer string. The dictionary should be sorted by key (character) in ascending order. Do not use built-in Python libraries or functions for sorting or character counting.
"""

def solve_string_problem(string1, string2):

    def count_characters(string):
        count_dict = {}
        for char in string:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        return count_dict

    def sort_dictionary(dictionary):
        sorted_dict = {}
        sorted_keys = list(dictionary.keys())
        sorted_keys.sort()
        for key in sorted_keys:
            sorted_dict[key] = dictionary[key]
        return sorted_dict

    string1_counts = count_characters(string1)
    string2_counts = count_characters(string2)

    string1_sorted = sort_dictionary(string1_counts)
    string2_sorted = sort_dictionary(string2_counts)

    if len(string1) > len(string2):
        return string1, string1_sorted
    else:
        return string2, string2_sorted