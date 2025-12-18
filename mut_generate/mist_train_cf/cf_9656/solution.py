"""
QUESTION:
Write a function called `sum_middle_elements` that takes a list of lists as input, where each sublist has at least three elements. The function should return a list of sums, where each sum is the result of adding the second and third elements of each sublist. The function should also print each sum before returning the list of sums.
"""

def sum_middle_elements(list_of_lists):
    """
    This function calculates the sum of the second and third elements of each sublist in a list of lists.
    
    Args:
        list_of_lists (list): A list of lists, where each sublist has at least three elements.
    
    Returns:
        list: A list of sums, where each sum is the result of adding the second and third elements of each sublist.
    """
    sums = []
    for sublist in list_of_lists:
        sum_of_middle_elements = sublist[1] + sublist[2]
        sums.append(sum_of_middle_elements)
        print(sum_of_middle_elements)
    return sums