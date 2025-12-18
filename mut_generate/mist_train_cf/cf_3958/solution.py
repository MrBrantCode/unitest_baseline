"""
QUESTION:
Create a function called `sort_list` that takes a list of integers as input. The function should remove any duplicate integers from the list and sort the remaining integers in descending order. The sorting algorithm used should have a time complexity of O(nlogn) and employ a divide and conquer approach. The function should not use any built-in sorting functions or methods.
"""

def sort_list(arr):
    # Remove duplicates from the list
    arr = list(set(arr))

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        
        return merge(left_half, right_half)

    def merge(left_half, right_half):
        result = []
        i = j = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                result.append(left_half[i])
                i += 1
            elif left_half[i] > right_half[j]:
                result.append(right_half[j])
                j += 1
            else:
                i += 1
                j += 1
        
        while i < len(left_half):
            result.append(left_half[i])
            i += 1
        
        while j < len(right_half):
            result.append(right_half[j])
            j += 1
        
        return result

    # Sort the list using merge sort in descending order
    arr = merge_sort(arr)
    arr.reverse()
    
    return arr