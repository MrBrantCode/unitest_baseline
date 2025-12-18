"""
QUESTION:
Write a function called `amplify_list_elements` that takes a multidimensional array as input, where each integer element is multiplied by 2, and returns the resulting array. The function should be able to handle arrays with any level of nesting.
"""

def amplify_list_elements(original_list):
    result = []
    for element in original_list:
        if type(element) is list:
            result.append(amplify_list_elements(element))
        else:
            result.append(element*2)
    return result