"""
QUESTION:
Sam is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile. Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne. 

Given an array of numbers, your function should return an array of arrays, where each subarray contains all the duplicates of a particular number. Subarrays should be in the same order as the first occurence of the number they contain:
Assume the input is always going to be an array of numbers. If the input is an empty array, an empty array should be returned.
"""

def group_duplicates(arr):
    """
    Groups all duplicates of each number in the input list into sublists, 
    maintaining the order of the first occurrence of each number.

    Parameters:
    arr (list of int or float): The input list of numbers.

    Returns:
    list of list of int or float: A list of sublists, where each sublist contains 
    all the duplicates of a particular number.
    """
    if not arr:
        return []
    
    seen = {}
    result = []
    
    for num in arr:
        if num not in seen:
            seen[num] = True
            result.append([num] * arr.count(num))
    
    return result