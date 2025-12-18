"""
QUESTION:
Implement the `quick_sort` function that sorts a given array list using the quick sort algorithm. The function should not take any additional parameters other than the list to be sorted. The input list will be modified in-place.
"""

def quick_sort(A):
    def partition_list(start, end):
        pivot = A[end]
        p_index = start
        for i in range(start, end):
            if A[i] <= pivot:
                A[i], A[p_index] = A[p_index], A[i]
                p_index += 1
        A[p_index], A[end] = A[end] , A[p_index]
        return p_index

    def quick_sort_helper(start, end):
        if start < end:
            p_index = partition_list(start, end)
            quick_sort_helper(start, p_index - 1)
            quick_sort_helper(p_index + 1, end)

    quick_sort_helper(0, len(A) - 1)