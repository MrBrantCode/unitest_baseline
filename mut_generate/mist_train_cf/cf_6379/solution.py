"""
QUESTION:
Write a function called `count_sum_pairs` that takes a list of integers `nums` and an integer `target` as input, and returns the number of pairs of elements in the list that sum to the target value, excluding duplicate pairs. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.
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