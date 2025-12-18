"""
QUESTION:
Write a function named `alternateSort` that takes an array of integers as input, sorts them in ascending order without using a direct sorting method or function, and reorders the array into a pattern where the first element is the smallest value, the second is the largest, the third is the second smallest, the fourth is the second largest, and so on.
"""

def alternateSort(arr):
    arr.sort() # sort array in ascending order
    i = 0 
    j = len(arr) - 1 
    result = [] 
    flag = True 
  
    while (i < j):
        if flag is True: 
            result.append(arr[i]) 
            i += 1
            flag = False
        else: 
            result.append(arr[j]) 
            j -= 1
            flag = True
    result.append(arr[i]) # append last element

    return result