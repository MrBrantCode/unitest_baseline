"""
QUESTION:
Implement a function named `list_operations` that takes two lists, `list1` and `list2`, and a list of operations to be performed on these lists. The function should return the results of the operations as a list. The operations to be performed are "merge", "common_elements", "unique_elements", "sort_in_descending", "element_difference", "length_of_list", "sum_of_elements", "average_of_elements", "max_element", and "min_element". If either of the input lists is empty, the function should return "Error: Empty list[s]". If an invalid operation is encountered, the function should return "Error: Invalid operation".
"""

def list_operations(list1, list2, operations):
    if len(list1) == 0 or len(list2) == 0:
        return "Error: Empty list[s]"
    result = []
    for operation in operations:
        if operation == "merge":
            result.append(sorted(list1 + list2, reverse=True))
        elif operation == "common_elements":
            result.append(sorted(list(set(list1) & set(list2)), reverse=True))
        elif operation == "unique_elements":
            result.append(sorted(list(set(list1) ^ set(list2)), reverse=True))
        elif operation == "sort_in_descending":
            result.append(sorted(list1 + list2, reverse=True))
        elif operation == "element_difference":
            result.append(sorted([abs(a - b) for a, b in zip(list1, list2)], reverse=True))
        elif operation == "length_of_list":
            result.append([len(list1), len(list2)])
        elif operation == "sum_of_elements":
            result.append([sum(list1), sum(list2)])
        elif operation == "average_of_elements":
            result.append([sum(list1)/len(list1), sum(list2)/len(list2)])
        elif operation == "max_element":
            result.append([max(list1), max(list2)])
        elif operation == "min_element":
            result.append([min(list1), min(list2)])
        else:
            return "Error: Invalid operation"
    return result