"""
QUESTION:
Implement a function `quick_sort(arr)` that sorts the given array in ascending order using the quick sort algorithm with the following requirements:

- The function should use recursion.
- The function should handle duplicate values in the array.
- The function should work with any data type.
- The function should have a time complexity of O(nlogn) in the average case.
- The function should use the first element in the array as the pivot.
- The function should handle edge cases such as empty arrays or arrays with only one element.
- The function should use an in-place sorting technique without creating additional arrays.
- The function should minimize the number of comparisons and swaps made.
- The function should minimize the stack space used during recursion.
"""

def quick_sort(arr):
    def _quick_sort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            _quick_sort(low, pivot_index - 1)
            _quick_sort(pivot_index + 1, high)

    def partition(low, high):
        pivot = arr[low]
        left = low + 1
        right = high

        done = False
        while not done:
            while left <= right and arr[left] <= pivot:
                left = left + 1
            while arr[right] >= pivot and right >=left:
                right = right -1
            if right < left:
                done= True
            else:
                arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]

        return right

    _quick_sort(0, len(arr) - 1)