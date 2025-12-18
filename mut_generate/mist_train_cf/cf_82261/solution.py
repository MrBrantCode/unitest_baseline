"""
QUESTION:
Write a function called `stringify_int_list` that takes a list of mixed data types as input, filters out non-integer elements, and returns a string of the remaining integers separated by a comma and a space. If an element is not an integer, print an error message indicating that the element will be ignored. Do not raise any exceptions.
"""

def stringify_int_list(lst):
    def check_integer(element):
        if isinstance(element, int):
            return True
        else:
            return False

    def convert_integer_to_string(element):
        return str(element)

    def concatenate_elements_to_string(lst):
        return ', '.join(lst)

    str_lst = []

    for element in lst:
        if check_integer(element):
            str_lst.append(convert_integer_to_string(element))
        else:
            print(f"Element {element} is not an integer and will be ignored.")

    return concatenate_elements_to_string(str_lst)