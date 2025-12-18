"""
QUESTION:
Write a function called `list_operations` that takes in two lists `list1` and `list2`, and a list of operations `operation_list`. The function should apply the operations specified in `operation_list` to `list1` and `list2`, and return the resulting lists. The operations can include "merge", "sort_in_descending", "remove_duplicates", "find_median", and other operations that you can implement similarly. If both lists are empty or if `operation_list` is empty, the function should return the original lists. If an operation is not defined, the function should print an error message.
"""

import statistics

def list_operations(list1, list2, operation_list):
    if not list1 and not list2:
        print("Both lists are empty.")
        return list1, list2
    if not operation_list:
        return list1, list2
    
    for operation in operation_list:
        if operation == "merge":
            list1.extend(list2)
            list2 = []
        elif operation == "sort_in_descending":
            list1.sort(reverse=True)
            if list2: list2.sort(reverse=True)
        elif operation == "remove_duplicates":
            list1 = list(set(list1))
            if list2: list2 = list(set(list2))
        elif operation == "find_median":
            if list2: 
                try: print(f"Median of list2: {statistics.median(list2)}")
                except statistics.StatisticsError: 
                    print("Can't find median of list2.")
            try: print(f"Median of list1: {statistics.median(list1)}")
            except statistics.StatisticsError: 
                print("Can't find median of list1.")
        # .., implement other operations similarly .., 
        else:
            print(f"Operation '{operation}' is not defined.")
    
    return list1, list2