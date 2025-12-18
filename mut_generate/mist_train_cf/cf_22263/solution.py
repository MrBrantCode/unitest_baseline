"""
QUESTION:
Write a function `remove_duplicates_sort_list` that takes a list as input and returns a new list with the following conditions met: 
1. All non-integer elements are removed from the list.
2. All duplicate integers are removed.
3. The remaining integers are sorted in descending order.
The function should be efficient enough to handle lists with up to 1,000,000 elements.
"""

def remove_duplicates_sort_list(input_list):
    unique_set = set()
    result = []
    
    for element in input_list:
        if isinstance(element, int):
            unique_set.add(element)
    
    for element in unique_set:
        result.append(element)
    
    result.sort(reverse=True)
    return result