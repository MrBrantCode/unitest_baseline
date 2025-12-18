"""
QUESTION:
Write a function `find_min_max` that takes an unsorted list of numbers as input and returns a tuple containing the smallest number, the largest number, and the count of the smallest and largest numbers. The function should have a time complexity of O(n log n) and should not use any built-in sorting functions. The function should handle duplicate numbers correctly.
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
        count_min = sum(1 for num in arr[left:right+1] if num == min_num)
        count_max = sum(1 for num in arr[left:right+1] if num == max_num)
        return min_num, max_num, (count_min, count_max)

    if len(arr) == 0:
        return None
    return find_min_max_helper(arr, 0, len(arr) - 1)