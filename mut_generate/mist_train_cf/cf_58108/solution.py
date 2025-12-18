"""
QUESTION:
Implement the function `unique_BST_sort(lst)` that sorts a list of integers and real numbers in a specific order using a Binary Search Tree (BST) approach. The sorting sequence should start with the smallest number, followed by the largest number from the remaining, then the smallest number not yet included from the remaining, and so on.
"""

def unique_BST_sort(lst):
    '''
    Upon a mixed assemblage of integers and real numbers, restore the list arrayed in a peculiar order employing Binary Search Tree (BST) tactic.
    The arraying sequence should adhere to the following progression:
    - Initiate with the least number.
    - Subsequently recognize the apex numeric from the remaining.
    - Proceed to decipher the least numerical not yet included from the remaining, and maintain this sequence.
    
    Demonstrations:
    unique_BST_sort([1, 2, 3, 4]) == [1, 4, 2, 3]
    unique_BST_sort([5, 5, 5, 5]) == [5, 5, 5, 5]
    unique_BST_sort([]) == []
    unique_BST_sort([-2, 1.5, 3.5, -1]) == [-2, 3.5, -1, 1.5]
    '''
    
    # sort values in ascending order
    lst.sort()
    result = []
    
    while lst: 
        # Pop the smallest value and append it to the result list
        result.append(lst.pop(0))
        
        # If there are values remaining, pop the largest value and append it to the result list
        if lst:
            result.append(lst.pop())
            
    return result