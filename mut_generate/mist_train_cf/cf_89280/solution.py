"""
QUESTION:
Write a function `find_min_max(arr)` that finds the smallest and largest numbers in an unsorted list `arr` with a time complexity of O(n log n) and returns the smallest number, the largest number, and the count of the smallest or largest number if it appears multiple times. Do not use any built-in sorting functions. The function should handle duplicate numbers correctly.
"""

def find_min_max(arr):
    def find_min_max_helper(arr, left, right):
        if left == right:
            return arr[left], arr[left], 1
        if left == right - 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right], 1
            else:
                return arr[right], arr[left], 1
        mid = (left + right) // 2
        min1, max1, count1 = find_min_max_helper(arr, left, mid)
        min2, max2, count2 = find_min_max_helper(arr, mid + 1, right)
        min_num = min(min1, min2)
        max_num = max(max1, max2)
        count = arr.count(min_num) if min_num == max_num else max(arr.count(min_num), arr.count(max_num))
        return min_num, max_num, count

    if len(arr) == 0:
        return None
    return find_min_max_helper(arr, 0, len(arr) - 1)