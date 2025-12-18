"""
QUESTION:
Implement the `merge_sort` and `heap_sort` functions that sort an arbitrary number of n numerical entities within an O(n log n) computational complexity timeframe. The input will be a list of integers, and the output should be a sorted list in ascending order.
"""

def merge_sort(nums):
    """Sorts an arbitrary number of n numerical entities in ascending order using the Merge Sort algorithm."""
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


def heapify(nums, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def heap_sort(nums):
    """Sorts an arbitrary number of n numerical entities in ascending order using the Heap Sort algorithm."""
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    return nums