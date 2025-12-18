"""
QUESTION:
Write a function named `bubble_sort_desc` that takes a list of numbers as input and returns the list sorted in descending order using the bubble sort algorithm. The function must not use any built-in Python sorting methods. Additionally, it must include error handling to check if the input is a list and if the list contains only numeric elements.
"""

def bubble_sort_desc(lst):
    # Check if input is a list
    if not isinstance(lst, list):
        return 'Error: Input must be a list'
    
    n = len(lst)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Check if elements are numeric
            try:
                float(lst[j])
                float(lst[j+1])
            except ValueError:
                return 'Error: Input list must contain only numeric elements'

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if lst[j] < lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst