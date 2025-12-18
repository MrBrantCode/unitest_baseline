"""
QUESTION:
Implement a function `merge_sort(dataset)` that sorts the given dataset using the merge sort algorithm and returns the number of comparisons made. The function should work for any duplicate values in the dataset.
"""

def merge_sort(dataset):
    comparison_counter = [0]
    merge_sort_helper(dataset, comparison_counter)
    return comparison_counter[0]

def merge_sort_helper(dataset, comparison_counter):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_half = dataset[:mid]
        right_half = dataset[mid:]

        merge_sort_helper(left_half, comparison_counter)
        merge_sort_helper(right_half, comparison_counter)

        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            comparison_counter[0] += 1
            if left_half[i] < right_half[j]:
                dataset[k] = left_half[i]
                i = i + 1
            else:
                dataset[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            dataset[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            dataset[k] = right_half[j]
            j = j + 1
            k = k + 1