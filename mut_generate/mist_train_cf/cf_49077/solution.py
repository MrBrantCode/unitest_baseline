"""
QUESTION:
Implement a merge sort function, `merge_sort`, that sorts an array in ascending order and handles duplicate values. The function should also keep track of the total number of comparisons made during the sorting process. The function should not modify the original array and should return the sorted array along with the total number of comparisons.
"""

def merge_sort(arr):
    """
    Sorts an array in ascending order and handles duplicate values.
    The function does not modify the original array and returns the sorted array along with the total number of comparisons.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        tuple: A tuple containing the sorted array and the total number of comparisons made during the sorting process.
    """
    comparisons = [0]

    def merge(left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            comparisons[0] += 1
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    def sort(arr):
        if len(arr) < 2:
            return arr
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        return merge(sort(left), sort(right))

    return sort(arr), comparisons[0]