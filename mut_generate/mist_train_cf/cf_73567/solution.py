"""
QUESTION:
Create a function named `modify_list` that takes in a list and an integer `k` as parameters. The function should return a new list that is a modified version of the input list based on the following rules: 

- If the list is empty, return a list containing only the integer `k`.
- If `k` is a non-negative integer, exclude the `k`th element from the list. If `k` exceeds the list's length, return the list in reverse order.
- If `k` is a negative integer, remove the `k`th element from the end of the list. Note that Python uses 0-based indexing for positive `k` and -1-based indexing from the end for negative `k`.
"""

def modify_list(lst, k):
    # Check for empty list
    if not lst:
        return [k]

    # Check if k is a positive integer
    if k >= 0: 
        if len(lst) > k:
            # Create new list excluding kth element
            return lst[:k] + lst[k+1:]
        else:
            # If k exceeds the list, return reversed list
            return lst[::-1]
    else: 
        # If k is a negative integer, remove kth element from end of the list
        return lst[:k] + lst[k+1:]