"""
QUESTION:
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.




Example 2:

Input: [1,2,2,3,1,4,2]
Output: 6



Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

def find_shortest_subarray_length_with_degree(nums):
    from collections import defaultdict
    
    # Step 1: Calculate the frequency of each element
    frequency = defaultdict(int)
    for num in nums:
        frequency[num] += 1
    
    # Step 2: Determine the degree of the array
    degree = max(frequency.values())
    
    # Step 3: If the degree is 1, the shortest subarray length is 1
    if degree == 1:
        return 1
    
    # Step 4: Find all elements that have the maximum frequency (degree)
    max_frequency_elements = [num for num, freq in frequency.items() if freq == degree]
    
    # Step 5: Calculate the shortest subarray length for each element with the maximum frequency
    min_length = float('inf')
    for element in max_frequency_elements:
        # Find the first and last occurrence of the element
        first_occurrence = nums.index(element)
        last_occurrence = len(nums) - 1 - nums[::-1].index(element)
        
        # Calculate the length of the subarray
        subarray_length = last_occurrence - first_occurrence + 1
        
        # Update the minimum length if this subarray is shorter
        if subarray_length < min_length:
            min_length = subarray_length
    
    return min_length