"""
QUESTION:
Construct a function named `custom_sort_list_mixed_types` that sorts a list containing both numeric values (including integers and floats) and string values. The function should separate the input list into two lists: one for numbers and one for strings, and sort each list in ascending order. If the input list contains only one type of data, the function should still return two lists, with the other list being empty. The function should not use any built-in sort() method or sorting function from a library.
"""

from typing import List, Union, Tuple

def custom_sort_list_mixed_types(my_list: List[Union[int, float, str]]) -> Tuple[List[Union[int, float]], List[str]]:
    num_list = [i for i in my_list if isinstance(i, (int, float))]
    str_list = [i for i in my_list if isinstance(i, str)]

    # Sorting num_list
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i]>num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]

    # Sorting str_list
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if str_list[i]>str_list[j]:
                str_list[i], str_list[j] = str_list[j], str_list[i]

    return num_list, str_list