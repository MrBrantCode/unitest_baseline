"""
QUESTION:
Implement a function called count_elements with the following requirements:
- The function should count the occurrences of each element in a given list of integers and return the counts.
- The function should have a time complexity of O(n) and a space complexity of O(k), where n is the number of elements in the list and k is the number of unique elements in the list.
- The function should only use a single loop to iterate through the list and should not use any built-in functions or data structures that directly solve the problem.
- The function should handle edge cases, including an empty list and a list containing only one element.
"""

def count_elements(nums):
    """
    This function counts the occurrences of each element in a given list of integers.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    list: A list containing the counts of each element in the input list.
    """
    if not nums:  # edge case: empty list
        return []
    
    if len(nums) == 1:  # edge case: list containing only one element
        return [1]
    
    nums.sort()  # sort the input list in non-decreasing order
    result = []  # list to store the counts of each element
    current_count = 1  # count of the current element being considered
    
    for i in range(1, len(nums)):  # iterate through the sorted list
        if nums[i] == nums[i - 1]:  # if the current element is equal to the next element
            current_count += 1  # increment the count of the current element
        else:  # if the current element is not equal to the next element
            result.append(current_count)  # append the count of the current element to the result list
            current_count = 1  # reset the count to 1
    
    result.append(current_count)  # append the count of the last element to the result list
    return result