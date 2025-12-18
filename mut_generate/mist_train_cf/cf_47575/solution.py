"""
QUESTION:
Design a function called `list_operations` that takes in three parameters: `list1` and `list2` containing integer elements, and `operations` containing a series of operations as strings. Perform the operations on `list1` and `list2` sequentially as they appear in `operations`, displaying the result of each operation in descending order of elements. Handle incorrect inputs and edge cases, including undefined operations, empty lists, and nested lists. 

The function should support the following operations: "merge", "common_elements", "unique_elements", "sort_in_descending", "element_difference", "length_of_list", "sum_of_elements", "average_of_elements", "max_element", "min_element". If an operation is not possible due to the nature of the lists, return an error message.
"""

def list_operations(list1, list2, operations):
    if len(list1) == 0 or len(list2) == 0:
        return "Error: Empty list(s)"
    result = []
    for operation in operations:
        if operation == "merge":
            result = sorted(list1 + list2, reverse=True)
        elif operation == "common_elements":
            result = sorted(list(set(list1) & set(list2)), reverse=True)
        elif operation == "unique_elements":
            result = sorted(list(set(list1) ^ set(list2)), reverse=True)
        elif operation == "sort_in_descending":
            result = sorted(list1 + list2, reverse=True)
        elif operation == "element_difference":
            if len(list1) != len(list2):
                return "Error: Lists must be of the same length for element difference"
            result = sorted([abs(a - b) for a, b in zip(list1, list2)], reverse=True)
        elif operation == "length_of_list":
            result = [len(list1), len(list2)]
        elif operation == "sum_of_elements":
            result = [sum(list1), sum(list2)]
        elif operation == "average_of_elements":
            result = [sum(list1) / len(list1), sum(list2) / len(list2)]
        elif operation == "max_element":
            result = [max(list1), max(list2)]
        elif operation == "min_element":
            result = [min(list1), min(list2)]
        else:
            return "Error: Invalid operation"
    return result