"""
QUESTION:
Merge two unsorted arrays into a single sorted array without using any extra space. The function should take two unsorted arrays, nums1 and nums2, as input and return the merged sorted array.
"""

def merge_arrays(nums1, nums2):
    # Iterate through each element in nums2
    for num2 in nums2:
        # Find the appropriate position to insert num2 in nums1
        for i, num1 in enumerate(nums1):
            if num2 < num1:
                nums1.insert(i, num2)
                break
        else:
            # If num2 is greater than all elements in nums1, insert it at the end
            nums1.append(num2)
    
    return nums1