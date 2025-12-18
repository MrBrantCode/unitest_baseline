"""
QUESTION:
Implement a function named `optimizedBubbleSort` that sorts an array using the Bubble Sort algorithm. The function should be adaptive, taking less time to sort an already sorted array by finishing in linear time complexity if the input array is already sorted. The function should take an array as input and return the sorted array.
"""

def optimizedBubbleSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, then the array is sorted.
        if swapped == False:
            break
    return arr