"""
QUESTION:
Write a function `odd_numbers` that takes a list as input and returns a list of odd integers in descending order. The input list may contain nested lists and non-integer values. The function should handle exceptions for non-integer inputs and return an error message if the input is not a list or if a non-integer value is found. The function should be able to handle large lists efficiently and should also be able to handle negative numbers.
"""

def odd_numbers(lst):
    if not isinstance(lst, list):
        return "Error: Input is not a list."
    
    try:
        flat_list = [i for sublist in lst for i in (sublist if isinstance(sublist, list) else [sublist])]
    
        odd_list = list(filter(lambda x: isinstance(x, int) and x % 2 != 0, flat_list))
        odd_list.sort(reverse=True)   
        
        return odd_list
        
    except Exception as e:
        return "Error: " + str(e)