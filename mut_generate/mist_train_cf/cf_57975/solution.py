"""
QUESTION:
Write a function `rearrange_array(arr)` that rearranges the input array of five unique integers between 1 and 15, such that every odd number is followed by an even number. If it's not possible to strictly follow this condition due to the number of odd and even elements, the function should return all odd numbers followed by an even number until possible, followed by the remaining numbers.
"""

def rearrange_array(arr):
    """
    This function rearranges the input array of unique integers between 1 and 15, 
    such that every odd number is followed by an even number. If it's not possible 
    to strictly follow this condition due to the number of odd and even elements, 
    the function returns all odd numbers followed by an even number until possible, 
    followed by the remaining numbers.

    Args:
        arr (list): A list of five unique integers between 1 and 15.

    Returns:
        list: The rearranged list.
    """
    odd = [x for x in arr if x%2 != 0]
    even = [x for x in arr if x%2 == 0]
    
    res = []
    while odd and even:
        res.append(odd.pop())
        res.append(even.pop())
    
    # adding remaining elements (if any)
    res = res + odd + even
    
    return res