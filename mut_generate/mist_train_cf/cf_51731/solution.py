"""
QUESTION:
Design a function `remove_and_shift(arr)` that takes a list `arr` as input and returns the modified list with all duplicate elements removed and the remaining elements shifted to the end, maintaining their original order. The function must be implemented in-place, without using any additional data structures.
"""

def remove_and_shift(arr): 
    if len(arr) <= 1: 
        return arr 

    j = 0
    
    for i in range(len(arr)): 
        k = 0
        while(k < i): 
            if (arr[i] == arr[k]): 
                break
            k += 1

        if (k == i): 
            arr[j] = arr[i] 
            j += 1

    for j in range(j,len(arr)):
        arr[j] = None

    return arr