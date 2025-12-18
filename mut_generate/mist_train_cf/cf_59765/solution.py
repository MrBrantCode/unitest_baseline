"""
QUESTION:
Create a function `perform_operations(list1, list2, operations)` that accepts three parameters: two lists of strings and a list of operations. The function should execute the operations in the order they appear in the operations list, where the operations can be "concatenation", "common_elements", "unique_elements", or "reverse_order". The result of each operation should be in alphabetical order. If the "unique_elements" operation cannot be performed due to identical input lists, return an error message.
"""

def perform_operations(list1, list2, operations):
    list1 = sorted(list1)
    list2 = sorted(list2)
    for operation in operations:
        if operation == 'concatenation':
            list1 = sorted(list1 + list2)
        elif operation == 'common_elements':
            list1 = sorted(list(set(list1).intersection(list2)))
        elif operation == 'unique_elements':
            if list1 == list2:
                return "Error: unique_elements operation cannot be performed as both lists are identical"
            list1 = sorted(list(set(list1).symmetric_difference(list2)))
        elif operation == 'reverse_order':
            list1 = list1[::-1]
    return list1