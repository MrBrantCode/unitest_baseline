"""
QUESTION:
Write a function named `count_numbers` that takes a list of integers (which may be nested) as input, and returns a dictionary where the keys are the unique integers and the values are their frequencies. The function should handle non-integer values by ignoring them, and should handle non-list inputs by returning an error message. The function should be implemented using recursion and should have a time complexity of O(n), where n is the total number of elements in the list (including nested lists).
"""

def count_numbers(input_list):
    if not isinstance(input_list, list):
        return "Input is not a list"
        
    count_dict = {}

    def helper_count(input_list):
        nonlocal count_dict

        for i in input_list:
            if isinstance(i, int):
                if i in count_dict:
                    count_dict[i] += 1
                else:
                    count_dict[i] = 1
            elif isinstance(i, list):
                helper_count(i)
    
    helper_count(input_list)
    
    return count_dict