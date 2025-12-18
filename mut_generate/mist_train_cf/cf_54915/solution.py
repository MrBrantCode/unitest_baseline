"""
QUESTION:
Implement a function `quick_sort` that sorts an array containing both integers and strings in ascending order using the quick-sort algorithm. The integers should be sorted numerically, and the strings should be sorted lexicographically. The input array is passed to the function along with the starting and ending indices of the array.
"""

def quick_sort(array, low, high):
    def partition(array, low, high):
        i = (low - 1)
        pivot = array[high]
        for j in range(low, high):
            if str(array[j]) <= str(pivot):
                i = i + 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return (i + 1)

    if low < high:
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index - 1)
        quick_sort(array, partition_index + 1, high)