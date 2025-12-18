"""
QUESTION:
Implement a function named `mergeSort` that sorts an input list of elements in ascending order using the Merge Sort algorithm, which has both average-case and worst-case time complexity of O(n log n). The function should take as input a list of elements and return the sorted list. The function should recursively divide the input list into two halves until each half has one element, and then merge the halves back together in the correct order.
"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j = j+1
            k = k+1
 
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i+1
            k = k+1
 
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j+1
            k = k+1
    return arr