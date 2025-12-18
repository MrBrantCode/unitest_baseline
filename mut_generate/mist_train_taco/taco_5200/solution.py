"""
QUESTION:
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].



Note:
The length of the input array will not exceed 20,000.
"""

from collections import Counter

def longest_harmonious_subsequence(nums):
    count = Counter(nums)
    max_length = 0
    for num in count:
        if num + 1 in count:
            max_length = max(max_length, count[num] + count[num + 1])
    return max_length