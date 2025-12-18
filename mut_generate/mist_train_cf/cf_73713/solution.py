"""
QUESTION:
Construct a function `list_operations` that takes three arguments: `list1` and `list2` which are lists containing integer elements (which can be nested), and `operations` which is a list of strings representing the sequence of operations to be performed on the lists. The function should execute the operations in the order they appear in the `operations` list and return the result of each operation in descending order. 

The allowed operations are: "merge", "common_elements", "unique_elements", "sort_in_descending", "element_difference", "length_of_list", "sum_of_elements", "average_of_elements", "max_element", "min_element", "flatten_nested_list", "remove_duplicates", "find_median", "find_mode", and "find_range". 

If an operation is infeasible due to the characteristics of the lists, the function should return a suitable error message. The function should also handle incorrect inputs, edge cases, and lists with mixed data types, and perform operations efficiently without causing a system crash or taking too much time.
"""

from typing import List, Union
from collections import Counter
import statistics

def list_operations(list1: List[Union[int, List[int]]], list2: List[Union[int, List[int]]], operations: List[str]) -> List[Union[int, str, float]]:
    if not list1 and not list2:
        return "Error: Lists cannot be empty"
    result = []
    for operation in operations:
        if operation == "merge":
            result = sorted(list1 + list2, reverse=True)
        elif operation == "common_elements":
            result = sorted(list(set(list1) & set(list2)), reverse=True)
        elif operation == "unique_elements":
            if list1 == list2:
                return "Error: Unique elements operation not possible as lists are identical"
            result = sorted(list(set(list1) ^ set(list2)), reverse=True)
        elif operation == "sort_in_descending":
            result = sorted(list1 + list2, reverse=True)
        elif operation == "element_difference":
            result = [abs(a-b) for a, b in zip(list1, list2)]
        elif operation == "length_of_list":
            result = len(list1 + list2)
        elif operation == "sum_of_elements":
            result = sum(list1 + list2)
        elif operation == "average_of_elements":
            result = statistics.mean(list1 + list2)
        elif operation == "max_element":
            result = max(list1 + list2)
        elif operation == "min_element":
            result = min(list1 + list2)
        elif operation == "flatten_nested_list":
            result = sorted(sum(list1 + list2, []), reverse=True)
        elif operation == "remove_duplicates":
            result = sorted(list(set(list1 + list2)), reverse=True)
        elif operation == "find_median":
            result = statistics.median(list1 + list2)
        elif operation == "find_mode":
            result = statistics.mode(list1 + list2)
        elif operation == "find_range":
            result = max(list1 + list2) - min(list1 + list2)
        else:
            return "Error: Undefined operation"
    if not operations:
        return list1, list2
    return result