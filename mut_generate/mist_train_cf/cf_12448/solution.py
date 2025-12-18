"""
QUESTION:
Create a function `count_elements` that takes a list of elements as input, where the elements can be of any type (strings, integers, lists, etc.). The function should return a dictionary where the keys are the unique elements from the input list and the values are the corresponding counts of each element. The function should be able to handle duplicate elements and count them correctly.
"""

def count_elements(input_list):
    count_dict = {}
    for element in input_list:
        if element not in count_dict:
            count_dict[element] = 1
        else:
            count_dict[element] += 1
    return count_dict