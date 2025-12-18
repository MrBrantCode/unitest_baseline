"""
QUESTION:
Write a function `findKthLargest` that takes two inputs: a list of integers and a positive integer `k`, and returns the kth largest element in the list. The input list can have up to 10^5 elements and may contain duplicate elements. The algorithm should have a time complexity of O(n) or better and a space complexity of O(1) or better. The list elements can range from -10^9 to 10^9.
"""

def findKthLargest(nums, k):
    def partition(nums, start, end):
        pivotIndex = start
        nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
        
        for i in range(start, end):
            if nums[i] > nums[end]:
                nums[i], nums[pivotIndex] = nums[pivotIndex], nums[i]
                pivotIndex += 1
        
        nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
        return pivotIndex

    start = 0
    end = len(nums) - 1
    
    while start <= end:
        pivotIndex = partition(nums, start, end)
        
        if pivotIndex == k - 1:
            return nums[pivotIndex]
        elif pivotIndex > k - 1:
            end = pivotIndex - 1
        else:
            start = pivotIndex + 1