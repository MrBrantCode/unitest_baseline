"""
QUESTION:
Design a function called `process_lists` that takes three parameters: two lists of integers and a list of operation strings. Perform the operations on the two lists sequentially as they appear in the operation list. The operations can be "merge", "common_elements", "unique_elements", "sort_in_descending", "element_difference", or "length_of_list". Return the result of each operation in descending order of elements. If an operation is not possible due to the nature of the lists, return an error message. Handle incorrect inputs and edge cases, including operations that are not defined, empty operation lists, and lists that do not contain any elements.
"""

def process_lists(list1, list2, operations):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Error: Both the first two inputs should be lists."
        
    if not all(isinstance(i, int) for i in list1+list2):
        return "Error: The first two lists should only contain integers."
        
    if not isinstance(operations, list) or not all(isinstance(i, str) for i in operations):
        return "Error: The third input should be a list of strings."
        
    if not list1 and not list2:
        return "Error: At least one of the first two lists should have elements."
        
    if not operations:
        return list1, list2
        
    result = []
    for op in operations:
        if op == "merge":
            result = sorted(list1 + list2, reverse=True)
        elif op == "common_elements":
            result = sorted(list(set(list1) & set(list2)), reverse=True)
        elif op == "unique_elements":
            if list1 == list2:
                return "Error: lists are identical, unique elements cannot be found."
            result = sorted(list(set(list1) ^ set(list2)), reverse=True)
        elif op == "sort_in_descending":
            result = sorted(list1 + list2, reverse=True)
        elif op == "element_difference":
            if len(list1) != len(list2):
                return "Error: cannot perform element difference, lists are of different length."
            result = sorted([a - b for a, b in zip(list1, list2)], reverse=True)
        elif op == "length_of_list":
            result = ["Length of list1 is " + str(len(list1)), 
                      "Length of list2 is " + str(len(list2))]
        else:
            return "Error: Unknown operation."
            
    return result