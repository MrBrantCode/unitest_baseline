"""
QUESTION:
Given a zero-indexed array A of length N containing distinct integers from 0 to N-1, write a function `arrayNesting(nums)` that returns the maximum length of a set S. The set S[i] is defined as {A[i], A[A[i]], A[A[A[i]]], ... } until a duplicate element appears. The function should operate within the constraint that N is an integer within the range [1, 20,000].
"""

def arrayNesting(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    visited = [0] * len(nums)
    max_length = 0 

    for i in range(len(nums)):
        if visited[i] == 0:
            start = nums[i]
            count = 0
            while True:
                start = nums[start]
                count += 1
                visited[start] = 1
                if start == nums[i]:
                    break
            max_length = max(max_length, count)

    return max_length