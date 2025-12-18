"""
QUESTION:
Create a function named `divide_lists` that takes two lists of numbers as input, `list1` and `list2`, and returns a new list where each element is the result of the division of the corresponding elements in `list1` and `list2`. 

The function should handle the following edge cases:
- Division by zero: if an element in `list2` is zero, the result should be 'Infinity' (or float('inf')).
- Non-numeric inputs: if an element in either list is not a number, the result should be 'Error: non-numeric input'.
- Lists of different lengths: if one list is shorter than the other, treat the missing elements in the shorter list as zeros by padding with zeros to match the length of the longer list.
"""

def divide_lists(list1, list2):
    len1, len2 = len(list1), len(list2)
    
    # Make the lists equal in length
    if len1 < len2:
        list1 += [0]*(len2-len1)
    elif len2 < len1:
        list2 += [0]*(len1-len2)
        
    result = []
    for i in range(len(list1)):
        try:
            # Check if the numerator and denominator are finite numbers
            if isinstance(list1[i], (int, float)) and isinstance(list2[i], (int, float)):
                if list2[i] != 0:
                    result.append(list1[i] / list2[i])
                else:
                    result.append('Infinity') # or use float('inf')
            else:
                result.append('Error: non-numeric input')
        except ZeroDivisionError:
            result.append('Infinity') # or use float('inf')

    return result