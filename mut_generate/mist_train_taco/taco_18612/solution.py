"""
QUESTION:
Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.
Example 1:
Input:
nums = {2, 8, 5, 4}
Output:
1
Explaination:
swap 8 with 4.
Example 2:
Input:
nums = {10, 19, 6, 3, 5}
Output:
2
Explaination:
swap 10 with 3 and swap 19 with 5.
Your Task:
You do not need to read input or print anything. Your task is to complete the function minSwaps() which takes the nums as input parameter and returns an integer denoting the minimum number of swaps required to sort the array. If the array is already sorted, return 0. 
Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ n ≤ 10^{5}
1 ≤ nums_{i} ≤ 10^{6}
"""

def min_swaps(nums):
    # Create a dictionary to store the index of each element in the original array
    index_map = {num: idx for idx, num in enumerate(nums)}
    
    # Sort the array and create a list of tuples (value, original_index)
    sorted_nums = sorted(nums)
    
    # Initialize the swap counter
    swaps = 0
    
    # Iterate through the sorted array
    for i in range(len(nums)):
        # Get the correct value that should be at index i
        correct_value = sorted_nums[i]
        
        # If the current value is not in the correct position
        if nums[i] != correct_value:
            # Find the index of the correct value in the original array
            correct_index = index_map[correct_value]
            
            # Swap the current value with the correct value
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
            
            # Update the index map after the swap
            index_map[nums[correct_index]] = correct_index
            index_map[nums[i]] = i
            
            # Increment the swap counter
            swaps += 1
    
    return swaps