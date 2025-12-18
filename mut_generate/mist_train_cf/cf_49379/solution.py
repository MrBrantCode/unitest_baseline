"""
QUESTION:
Implement a function named `rearrange_three_elements` that takes a list of integers `arr` as input and returns `True` if it's possible to generate a non-decreasingly sorted array by performing a maximum of three transpositions of exactly two elements, and ensuring the final array has an odd number of elements lesser than the first element in the original array. Return `False` otherwise. Assume any number of right-shift operations can be performed.
"""

def rearrange_three_elements(arr):
    def sort_by_swap(arr, n):
        swap_count = 0
        for i in range(n):
            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    swap_count += 1
        return swap_count

    # Handle case of empty array
    if not arr:
        return True

    num_swaps = sort_by_swap(arr, len(arr))
    lesser_than_first_element = [x for x in arr if x < arr[0]]

    # Check if number of swaps is within limit and ensure final array has odd number of elements lesser than first element
    if num_swaps <= 3 and len(lesser_than_first_element) % 2 == 1:
        return True
    else:
        return False