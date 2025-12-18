"""
QUESTION:
Given integer arrays `arr` and `add`, and a target value `target`, write a function `findBestValue(arr, add, target)` that returns the integer `value` such that when we change all the integers larger than `value` in the given arrays to be equal to `value`, the sum of the arrays gets as close as possible (in absolute difference) to `target`. In case of a tie, return the minimum such integer. The answer is not necessarily a number from `arr` or `add`. The constraints are `1 <= arr.length, add.length <= 10^4` and `1 <= arr[i], add[i], target <= 10^5`.
"""

def findBestValue(arr, additional, target):
    def binary_search(left, right):
        while left < right:
            mid = (left + right) // 2
            if sum(min(x, mid) for x in arr + additional) < target:
                left = mid + 1
            else:
                right = mid
        return left

    max_val = max(arr + additional)
    return binary_search(1, max_val)