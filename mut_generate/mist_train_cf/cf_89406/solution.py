"""
QUESTION:
Create a function called `count_sum_pairs` that takes two parameters: a list of integers `nums` and a target integer `target`. The function should return the number of unique pairs of elements in `nums` that sum to `target`. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of `nums`. The length of `nums` will not exceed 10^5 integers and the elements in `nums` and `target` will be in the range of -10^5 to 10^5.
"""

def count_sum_pairs(nums, target):
    # Create a dictionary to store the frequency of each element in the list
    num_freq = {}
    count = 0

    # Iterate through each element in the list
    for num in nums:
        # Calculate the complement of the current element with respect to the target
        complement = target - num

        # Check if the complement exists in the dictionary and is not zero
        if complement in num_freq and num_freq[complement] > 0:
            # Increment the count by the frequency of the complement
            count += num_freq[complement]
        
        # Increment the frequency of the current element in the dictionary
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
    
    # Return the count of unique pairs
    return count