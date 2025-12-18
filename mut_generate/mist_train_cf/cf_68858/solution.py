"""
QUESTION:
Create a function `quartiles` that calculates the first and third quartiles of a given tuple consisting of both even and odd numbers. The function should not use list sorting or built-in functions or algorithms for sorting. It should handle tuples of both even and odd lengths, and return the first and third quartiles as a tuple.
"""

def quartiles(lst):
    def median(lst):
        n = len(lst)
        if n % 2 == 1:
            return findKthLargest(lst, n // 2)
        else:
            return 0.5 * (findKthLargest(lst, n // 2 - 1) + findKthLargest(lst, n // 2))

    def findKthLargest(nums, k):
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        if k < len(left):
            return findKthLargest(left, k)
        elif k < len(left) + len(mid):
            return nums[k]
        else:
            return findKthLargest(right, k - len(left) - len(mid))

    n = len(lst)
    if n % 2 == 1:
        return (findKthLargest(lst, n // 4), findKthLargest(lst, n * 3 // 4))
    else:
        return (0.5 * (findKthLargest(lst, n // 4 - 1) + findKthLargest(lst, n // 4)),
                0.5 * (findKthLargest(lst, n * 3 // 4 - 1) + findKthLargest(lst, n * 3 // 4)))