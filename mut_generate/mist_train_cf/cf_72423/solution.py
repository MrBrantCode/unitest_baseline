"""
QUESTION:
Given a sorted array `nums` that is not directly accessible and an integer `k`, return the `kth` missing number starting from the leftmost number of the array using an API `read(int index)` that returns the element at the given index. The array `nums` is sorted in ascending order and all its elements are unique. `1 <= nums.length <= 5 * 104`, `1 <= nums[i] <= 107`, and `1 <= k <= 108`. Find a solution with a logarithmic time complexity (i.e., `O(log(n))`) that calls the API `read(int index)` at most `log(n)` times.
"""

def findKthPositive(read, k):
    # establish upper bound for our binary search
    upper = 1
    while read(upper) != -1 and read(upper) - upper - 1 < k:
        upper *= 2

    # binary search to home in on kth missing number
    lower = upper // 2
    while lower < upper:
        mid = (lower + upper) // 2
        if read(mid) == -1 or read(mid) - mid - 1 < k:
            lower = mid + 1
        else:
            upper = mid
                
    return lower + k