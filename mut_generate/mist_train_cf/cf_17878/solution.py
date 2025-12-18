"""
QUESTION:
Write a function `find_longest_sequences(nums)` that takes a list of integers `nums` as input, where the length of `nums` does not exceed 10^6 and the integers in `nums` range from -10^6 to 10^6. The function should return all distinct longest continuous increasing sequences of integers within `nums` with a time complexity of O(n) and a space complexity of O(1), excluding the space required for the output.
"""

def find_longest_sequences(nums):
    if len(nums) == 0:
        return []
    
    result = []
    longest_seq = [nums[0]]
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            longest_seq.append(nums[i])
        else:
            if len(longest_seq) > 1:
                result.append(longest_seq)
            longest_seq = [nums[i]]
    
    if len(longest_seq) > 1:
        result.append(longest_seq)
    
    return result