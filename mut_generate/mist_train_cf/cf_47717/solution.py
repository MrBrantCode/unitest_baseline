"""
QUESTION:
Create a function named `count_occurrences` that takes two parameters: a list `lst` and a list `elements`. The function should count the occurrences of each element in `elements` within the list `lst` and return a dictionary where the keys are the elements to be counted and the values are their corresponding counts. The function should only count elements that are present in the `elements` list.
"""

def count_occurrences(lst, elements):
    count_dict = {element: 0 for element in elements}
    for ele in lst:
        if ele in count_dict:
            count_dict[ele] += 1
    return count_dict