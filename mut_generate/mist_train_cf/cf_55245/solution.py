"""
QUESTION:
Create a function named `strange_sort_list_bst` that accepts a list of integers and decimal numbers, and returns the list in a specific pattern. The pattern starts with the smallest number, followed by the largest value from the remaining elements, then the smallest value from the remaining elements, and so on, alternating between the smallest and largest values. The function should handle empty lists and lists with duplicate values.
"""

def strange_sort_list_bst(lst):
    '''
    This function accepts a list of integers and decimal numbers and returns the list in a specific pattern, 
    alternating between the smallest and largest values.
    '''
    
    lst.sort()
    output = []

    while lst:
        output.append(lst.pop(0))  # smallest
        if lst:
            output.append(lst.pop(-1))  # largest

    return output