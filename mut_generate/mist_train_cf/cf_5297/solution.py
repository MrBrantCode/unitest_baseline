"""
QUESTION:
Implement a function named `solve` that takes a set of integers as input, calculates the number of positive numbers, their average, maximum, minimum, and median, and returns these values.

Constraints:
- The input set can contain up to 10^7 elements.
- Each element in the set is an integer ranging from -10^9 to 10^9.
- The median is the middle element when the positive numbers are arranged in ascending order.
- You are not allowed to use any built-in sorting functions or data structures; instead, implement your own sorting algorithm, such as Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, or Merge Sort, to find the median of the positive numbers.
"""

def merge_sort(arr):
    """Recursively divides the array into two halves until each sub-array contains one element, 
    and then merges adjacent sorted sub-arrays to produce the final sorted array."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    """Merges two sorted arrays into a single sorted array."""
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def solve(nums):
    """Calculates the number of positive numbers, their average, maximum, minimum, and median."""
    positive_nums = []
    total = 0
    count = 0
    max_num = float('-inf')
    min_num = float('inf')
    for num in nums:
        if num > 0:
            positive_nums.append(num)
            total += num
            count += 1
            max_num = max(max_num, num)
            min_num = min(min_num, num)
    if count == 0:
        return 0, 0, 0, 0, 0
    average = total / count
    sorted_positive_nums = merge_sort(positive_nums)
    if count % 2 == 1:
        median = sorted_positive_nums[count // 2]
    else:
        mid1 = sorted_positive_nums[count // 2 - 1]
        mid2 = sorted_positive_nums[count // 2]
        median = (mid1 + mid2) / 2
    return count, average, max_num, min_num, median