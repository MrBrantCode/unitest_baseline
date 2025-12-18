"""
QUESTION:
Design a function `interchange_and_compute(list1, list2)` that takes two lists of integers as input. The function should interchange the elements of the two lists while keeping the same index for each number, then compute the mean and median of the elements in each list individually. The function should return the two modified lists, along with their respective mean and median. The input lists must not be empty and must have the same length.
"""

def interchange_and_compute(list1, list2):
    # Check if list1 and list2 are empty
    if not list1 or not list2:
        return "Input lists must not be empty." 
    
    # Check if list1 and list2 have the same length
    if len(list1) != len(list2):
        return "Input lists must have the same length."
    
    # Interchange elements
    list1[:], list2[:] = list2[:], list1[:]
    
    # Compute mean
    mean1 = sum(list1) / len(list1)
    mean2 = sum(list2) / len(list2)
    
    # Compute median
    list1.sort()
    list2.sort()
    
    if len(list1) % 2 == 0:
        median1 = (list1[len(list1)//2] + list1[len(list1)//2 - 1]) / 2
    else:
        median1 = list1[len(list1)//2]
        
    if len(list2) % 2 == 0:
        median2 = (list2[len(list2)//2] + list2[len(list2)//2 - 1]) / 2
    else:
        median2 = list2[len(list2)//2]
        
    return (list1, mean1, median1, list2, mean2, median2)