"""
QUESTION:
Write a function called `sort_multidimensional_array` that sorts elements in a multidimensional array from smallest to largest values. The function should first sort elements within each sub-array using the cocktail shaker sort method, and then sort the sub-arrays themselves based on their first element. The function should be able to handle non-square arrays and situations where different sub-arrays may contain different numbers of elements.
"""

def cocktail_shaker_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        is_swapped = False

        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                is_swapped = True

        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True

        if not is_swapped:
            return arr
            
    return arr            

def sort_multidimensional_array(arr):
    for i in range(len(arr)):
        arr[i] = cocktail_shaker_sort(arr[i])

    arr = sorted(arr, key=lambda x: x[0])

    return arr