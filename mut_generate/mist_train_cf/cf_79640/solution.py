"""
QUESTION:
Write a function named `find_rarest_element` that takes a list of elements as input and returns a list of the rarest elements in the input list. The function should handle the case where there are multiple elements with the same lowest frequency. If the input list is empty, the function should return `None`.
"""

def find_rarest_element(input_list):
    if not input_list:
        return None
    count_dict = {}
    for elem in input_list:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    min_count = min(count_dict.values())
    rarest_elements = [k for k, v in count_dict.items() if v == min_count]
    return rarest_elements