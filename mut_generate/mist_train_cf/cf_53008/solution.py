"""
QUESTION:
Implement a hybrid quicksort function, `quick_sort(arr)`, that sorts a list of integers. The function should switch to insertion sort when the length of the sublist is 10 or less. The pivot should be chosen using the "median of three" method to prevent worst-case O(n²) runtime. The function should take no arguments other than the input list `arr` and return the sorted list.
"""

def quick_sort(arr):
    if len(arr) <= 10: 
        return insertion_sort(arr)
    else:
        pivot = median_of_three(arr) 
        less = [x for x in arr[1:] if x <= arr[pivot]]
        greater = [x for x in arr[1:] if x > arr[pivot]]
        return quick_sort(less) + [arr[pivot]] + quick_sort(greater)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def median_of_three(arr):
    mid = len(arr) // 2
    s = sorted([arr[0], arr[mid], arr[-1]]) 
    return arr.index(s[1])