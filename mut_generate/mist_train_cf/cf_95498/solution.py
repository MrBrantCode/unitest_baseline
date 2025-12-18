"""
QUESTION:
Create a function `count_occurrences` that takes three parameters: a list `lst`, an element, and a data type. The function should count the occurrences of the given element in the list, ignoring any occurrences within nested sublists, and only considering elements of the specified data type. The function should return the total count of occurrences.
"""

def count_occurrences(lst, element, data_type):
    count = 0
    
    def count_element(lst):
        nonlocal count
        
        for item in lst:
            if isinstance(item, list):
                count_element(item)  
            elif isinstance(item, data_type) and item == element:
                count += 1
    
    count_element(lst)
    return count