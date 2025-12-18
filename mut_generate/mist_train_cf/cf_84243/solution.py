"""
QUESTION:
Create a function named `odd_count_elements` that takes two lists of integers as input and returns a list of integers. The function should return a list of elements that appear an odd number of times in the combined list of the two input lists, sorted in descending order.
"""

def odd_count_elements(list1: list, list2: list) -> list:
    """
    This function takes two lists of integers as input, 
    and returns a list of integers that appear an odd number of times 
    in the combined list of the two input lists, sorted in descending order.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        list: A list of integers that appear an odd number of times in the combined list, sorted in descending order.
    """
    dict_count = {}
    for item in list1 + list2:
        if item in dict_count:
            dict_count[item] += 1
        else:
            dict_count[item] = 1

    odd_count_elements = [key for key, value in dict_count.items() if value % 2 != 0]

    # bubble sort in descending order
    for _ in range(len(odd_count_elements)):
        for i in range(len(odd_count_elements) - 1):
            if odd_count_elements[i] < odd_count_elements[i + 1]:
                odd_count_elements[i], odd_count_elements[i + 1] = odd_count_elements[i + 1], odd_count_elements[i]
                
    return odd_count_elements