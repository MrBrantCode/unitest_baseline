"""
QUESTION:
Implement a function called `merge_sort` that sorts a given list of integers in descending order using the merge sort algorithm. The function should not use any built-in sorting functions. The input list is a collection of integers, and the output should be the sorted list in descending order.
"""

def merge_sort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_half = dataset[:mid]
        right_half = dataset[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:  
                # Modifying the condition for descending
                dataset[k] = left_half[i]
                i = i + 1
            else:
                dataset[k] = right_half[j]
                j = j + 1
            k = k + 1

        # For all the remaining values
        while i < len(left_half):
            dataset[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            dataset[k] = right_half[j]
            j = j + 1
            k = k + 1
    return dataset