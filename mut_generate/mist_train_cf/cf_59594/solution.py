"""
QUESTION:
Write a function called `dict_element_sum` that takes a dictionary with string keys and list values as input. Each list contains at least two numerical elements. The function should return a new dictionary with the same keys as the input dictionary. For each key, the corresponding value in the output dictionary is a list of sums of all pairs of adjacent elements in the input list. For example, given the input {'X': [11, 22, 33], 'Y': [44, 55, 66], 'Z': [77, 88, 99]}, the output should be {'X': [33, 55], 'Y': [99, 121], 'Z': [165, 187]}.
"""

def dict_element_sum(dict_input):
    dict_output = {}
    for key in dict_input:
        dict_output[key] = [dict_input[key][i] + dict_input[key][i+1] for i in range(len(dict_input[key])-1)]
    return dict_output