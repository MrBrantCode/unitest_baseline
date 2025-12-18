"""
QUESTION:
Implement a function named `sort_data` that takes a list of mixed data types as input. The function should return the list with all strings sorted alphabetically and dictionaries with their keys sorted alphabetically, while ignoring integers and other data types. The function should not use built-in Python sorting functions and instead implement the sorting algorithm manually.
"""

def sort_data(data):
    # calling bubble sort function for sorting strings
    strings = bubble_sort([item for item in data if isinstance(item, str)]) 
    # sorting keys of dictionary  
    dicts = [dict(sorted(item.items())) for item in data if isinstance(item, dict)] 
    others = [item for item in data if not isinstance(item, str) and not isinstance(item, dict)]
  
    return strings + dicts + others

def bubble_sort(data):
    n = len(data)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
            
            # Traverse through 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element                   
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
    return data