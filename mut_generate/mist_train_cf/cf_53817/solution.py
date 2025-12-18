"""
QUESTION:
Create a function `nextGreaterElement(nums1, nums2)` that finds all the next greater numbers for `nums1`'s elements in the corresponding places of `nums2`. The Next Greater Number of a number `x` in `nums1` is the first greater number to its right in `nums2`. If it does not exist, return `-1` for this number, along with its index `-1`. The function should have a time complexity of `O(nums1.length + nums2.length)`.

`nums1` and `nums2` are two integer arrays of unique elements, where `nums1` is a subset of `nums2`. The length of `nums1` and `nums2` is between `1` and `1000`, and all integers in both arrays are between `0` and `10^4`.
"""

def nextGreaterElement(nums1, nums2):
    stack = []
    d = {} 
    for n in nums2[::-1]: 
        while stack and stack[-1] <= n: 
            stack.pop() 
        if stack:
            d[n] = [stack[-1], nums2.index(stack[-1])]
        else:
            d[n] = [-1, -1]
        stack.append(n)
    return [d[n] for n in nums1]