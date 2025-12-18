"""
QUESTION:
Write a function `decompose_and_count` that takes a multi-level list of integers as input, counts the occurrences of each unique integer in the list, and returns a dictionary where the keys are the unique integers and the values are their respective frequencies. The input list may contain nested lists of arbitrary depth.
"""

def decompose_and_count(lst):
    freq_dict = {}

    def recursive_helper(sub_lst):
        for element in sub_lst:
            if type(element) is list:
                recursive_helper(element)
            else:
                if element in freq_dict:
                    freq_dict[element] += 1
                else:
                    freq_dict[element] = 1

    recursive_helper(lst)
    return freq_dict