"""
QUESTION:
Implement a function `strange_sort_list_bst` that accepts a list of integers and decimal numbers and returns the list in a specific pattern, leveraging the principles of a binary search tree. The steps to this pattern should be: 
- Commence with the smallest number.
- Next, identify the highest value from the remaining elements.
- Then, ascertain the lowest value among the untouched output, and continue in this manner.
 
Restrictions: The function should work for both empty and non-empty lists, and handle lists containing duplicate numbers.
"""

def strange_sort_list_bst(lst):
    lst.sort()
    output = []
    while lst:
        output.append(lst.pop(0))  
        if lst:
            output.append(lst.pop(-1))  
    return output