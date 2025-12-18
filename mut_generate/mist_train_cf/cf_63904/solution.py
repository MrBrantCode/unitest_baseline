"""
QUESTION:
Create a function named `FunctionB` that takes a list of elements as input. The function should return a list of unique integers from the input list that are less than 50, in descending order. If the input list contains non-integer values, the function should ignore them.
"""

def entrance(lst):
    #Converting list to set for distinct values
    lst = set(lst)
    result = []
    
    for num in lst:
        #Checking for non-integer input
        if isinstance(num, int) and num < 50:
            result.append(num)
    
    #Sorting the list in descending order
    result = sorted(result, reverse=True)
    return result