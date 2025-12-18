"""
QUESTION:
Write a function 'divideList' that takes a list of integers and a positive integer 'n', and divides the list into 'n' groups. The elements in the sublists should maintain their original order. If the list cannot be divided evenly, the function should attempt to balance the elements as much as possible between groups, but the final group may have less than the others. The function should handle potential exceptions or errors, such as division by zero, negative 'n', or an empty list, and return an error message or an empty list accordingly.
"""

import math

def divideList(inputList, n):
    if n <= 0:
        return "Error: n should be a positive integer"
        
    length = len(inputList)
    if length == 0:
        return []
        
    avg = math.ceil(length / float(n))
    out = []
    last_index = 0
    for _ in range(n):
        if last_index + avg <= length:
            out.append(inputList[last_index:last_index+avg])
            last_index += avg
        else:
            out.append(inputList[last_index:length])
            break

    return out