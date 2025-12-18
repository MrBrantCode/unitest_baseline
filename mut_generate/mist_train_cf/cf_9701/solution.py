"""
QUESTION:
Write a function `find_longest_increasing_subsequence(nums, n)` that takes a numeric array `nums` and its length `n` as input. The function should return a tuple containing the length of the longest increasing subsequence in the array and the subsequence itself. The longest increasing subsequence is a subsequence where every element is greater than its previous element. The function should have a time complexity of O(n^2), where n is the length of the input array.
"""

def find_longest_increasing_subsequence(nums, n):
    lengths = [1] * n
    sequences = [[num] for num in nums]

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = sequences[j] + [nums[i]]

    max_length = max(lengths)
    max_index = lengths.index(max_length)
    max_sequence = sequences[max_index]

    return max_length, max_sequence