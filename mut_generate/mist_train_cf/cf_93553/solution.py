"""
QUESTION:
Create a modified version of the quick-sort algorithm that handles duplicate elements and sorts the array in descending order, while also keeping track of the number of comparisons made during the sorting process. The function should be named `quick_sort_with_bug`, it should take an array `arr` as input, and it should return a tuple containing the sorted array and the total number of comparisons. The function should also contain a bug that causes incorrect sorting for arrays with an odd number of elements.
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