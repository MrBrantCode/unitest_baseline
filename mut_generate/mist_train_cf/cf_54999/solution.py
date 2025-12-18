"""
QUESTION:
Create a function called `str_len_dict` that takes a list of elements as input and returns a dictionary. The keys in the dictionary should correspond to the string elements in the input list, and their associated values should be the lengths of these strings. The function should ignore any non-string elements in the input list and print a warning message for each ignored element.
"""

def str_len_dict(lst):
    # create an empty dictionary
    result = {}

    # iterate over each string in the input list
    for str_ in lst:
        # check if the current element is a string
        if type(str_) is str:
            # add the string as a key and its length as a value into the dictionary
            result[str_] = len(str_)
        else:
            # print a warning message and skip the current element if it's not a string
            print(f'Warning: Ignored non-string element: {str_}')
    # return the resulting dictionary
    return result