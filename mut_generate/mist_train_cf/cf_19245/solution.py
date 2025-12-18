"""
QUESTION:
Implement a recursive Merge Sort algorithm to sort an unsorted array of numbers in ascending order without using any comparison-based sorting algorithm or extra space for merging the arrays. The function should be named `mergeSort` and take as parameters an array `arr` and two integers `l` and `r` representing the left and right bounds of the array.
"""

def merge(arr, start, mid, end):
    start2 = mid + 1
    
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
    
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
        
        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
            
            # Shift all the elements between element 1
            # and element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
                
            arr[start] = value
            
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

def mergeSort(arr, l, r):
    if (l < r):
        
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
        
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        
        merge(arr, l, m, r)