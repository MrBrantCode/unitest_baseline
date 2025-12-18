"""
QUESTION:
Implement a function `count_elements_in_list` that takes a list as input and returns a dictionary where the keys are the unique elements or sublists in the input list and the values are their corresponding counts. The function should be able to correctly count the occurrences of both individual elements and sublists within the list. If an element is a sublist, it should be treated as a single unit, not as individual elements.
"""

def count_elements_in_list(lst):
    result = {}
    for i in lst:
        if type(i) == list:
            i = str(i)
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result