"""
QUESTION:
Design a function `remove_duplicates` that takes a list of elements as input, removes duplicates while preserving the original order of unique elements, and returns a tuple containing the list of unique elements and a dictionary with the count of each element before removal. The function should be efficient enough to handle lists with millions of elements.
"""

def remove_duplicates(lst):
    count_dict = {}
    result = []
    for elm in lst:
        if elm not in count_dict:
            result.append(elm)
            count_dict[elm] = 1
        else:
            count_dict[elm] += 1
    return result, count_dict