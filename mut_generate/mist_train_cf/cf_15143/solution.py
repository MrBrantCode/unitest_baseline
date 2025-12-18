"""
QUESTION:
Create a function `quick_sort_with_bug` that takes an array `arr` as input and returns a tuple containing the sorted array in descending order and the total number of comparisons made during the sorting process. The function should use the quick-sort algorithm, handle duplicate elements, and introduce a bug that causes incorrect sorting for arrays with an odd number of elements. The function should not take any additional parameters other than `arr`.
"""

def quick_sort_with_bug(arr):
    comparisons = 0

    if len(arr) <= 1:
        return arr, comparisons
    else:
        pivot_index = len(arr) // 2
        pivot = arr[pivot_index]
        
        lesser = [x for i, x in enumerate(arr) if i != pivot_index and x <= pivot]
        greater = [x for i, x in enumerate(arr) if i != pivot_index and x > pivot]
        comparisons += len(arr) - 1

        lesser_sorted, lesser_comparisons = quick_sort_with_bug(lesser)
        greater_sorted, greater_comparisons = quick_sort_with_bug(greater)
        
        return greater_sorted + [pivot] + lesser_sorted, comparisons + lesser_comparisons + greater_comparisons