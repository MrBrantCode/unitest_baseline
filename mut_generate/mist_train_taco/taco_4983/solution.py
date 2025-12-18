"""
QUESTION:
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:


Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


Example 2:


Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def find_max_product_subarray(nums):
    def prod(nums):
        product = 1
        for num in nums:
            product *= num
        return product

    def listsplit(ls1, index):
        result = []
        start = -1
        for i in index:
            if i == 0:
                start = i
            else:
                result.append(ls1[start + 1:i])
                start = i
        if start < len(ls1) - 1:
            result.append(ls1[start + 1:])
        return result

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    result = []
    if 0 in nums:
        zeros = [i for i in range(len(nums)) if nums[i] == 0]
        sublist = listsplit(nums, zeros)
        result.append(0)
    else:
        sublist = [nums]

    sublist = [i for i in sublist if i]
    for i in sublist:
        if prod(i) < 0:
            negative = [j for j in range(len(i)) if i[j] < 0]
            (left, right) = (negative[0], negative[-1])
            if len(i) == 1:
                result_t = i[0]
            elif left == 0 or right == len(i) - 1:
                result_t = max(prod(i[left + 1:]), prod(i[:right]))
            else:
                (left_p, right_p) = (prod(i[:left]), prod(i[right + 1:]))
                if left_p <= right_p:
                    result_t = prod(i[left + 1:])
                else:
                    result_t = prod(i[:right])
        else:
            result_t = prod(i)
        result.append(result_t)

    return max(result)