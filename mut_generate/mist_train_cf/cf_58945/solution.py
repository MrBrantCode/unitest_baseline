"""
QUESTION:
Create a function called 'median' that takes two parameters: a list 'l' and a comparison function 'cmp_func'. The function should calculate the middle value of the list 'l' without using sorting or built-in functions. It should handle lists with both even and odd numbers of elements and remove duplicate values. The comparison function 'cmp_func' should be used to compare elements in the list. The function should return the median value.
"""

def median(l: list, cmp_func: callable):
    """
    Calculate the middle value of a list without using sorting or built-in functions.

    Parameters:
    l (list): The input list
    cmp_func (callable): A comparison function to compare elements in the list

    Returns:
    The median value of the list
    """
    
    # Remove any duplicate entries for correctness purpose
    l = list(dict.fromkeys(l))
    
    # Get Length of the list
    n = len(l)
    
    # Median calculation for even length lists
    if n % 2 == 0:
        left, right = None, None
        for i in l:
            less = len([j for j in l if cmp_func(j, i) < 0])
            equal = len([j for j in l if cmp_func(j, i) == 0])
            if less <= n // 2 - 1 < less + equal:
                left = i
            if less <= n // 2 < less + equal:
                right = i
                break

        return (left + right) / 2

    # Median calculation for odd length lists
    else:
        for i in l:
            less = len([j for j in l if cmp_func(j, i) < 0])
            equal = len([j for j in l if cmp_func(j, i) == 0])
            if less <= n // 2 < less + equal:
                return i