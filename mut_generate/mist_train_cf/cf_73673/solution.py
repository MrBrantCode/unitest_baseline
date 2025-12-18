"""
QUESTION:
Write a function `unique_in_list` that takes a list of lists, including nested lists, as input. The function should flatten the nested lists, treat their elements as part of the main list, and return a list of unique elements. The function should not preserve the original order of elements and can use any data structure available in Python.
"""

def unique_in_list(lists):
    def flatten(input_list):
        output_list = []
        for i in input_list:
            if type(i) == list:
                output_list.extend(flatten(i))
            else:
                output_list.append(i)
        return output_list

    flat_list = flatten(lists)
    return list(set(flat_list))