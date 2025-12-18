"""
QUESTION:
Implement a function `bubble_sort_negative_descending(arr)` that sorts a given array of numbers in descending order using the bubble sort algorithm. The function should handle duplicate numbers by maintaining their original order relative to other duplicate numbers. Additionally, it should place negative numbers at the beginning of the sorted array in descending order.
"""

def bubble_sort_negative_descending(arr):
    length = len(arr)
    swapped = True
    pass_num = 1
    while swapped:
        swapped = False
        i = 0
        while i < length - pass_num:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            i += 1
        pass_num += 1
    i = 0
    while i < length:
        if arr[i] < 0:
            for j in range(length):
                if arr[j] > 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
        i += 1
    return arr