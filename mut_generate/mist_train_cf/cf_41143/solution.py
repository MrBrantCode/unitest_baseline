"""
QUESTION:
Write a function `longestConsecutive` that takes a list of integers `nums` and returns the length of the longest consecutive elements sequence in the list. A consecutive sequence is a sequence of numbers where each number appears exactly once and the difference between consecutive numbers is 1. The function should return an integer representing the length of the longest consecutive sequence.
"""

def longestConsecutive(nums):
    s = set(nums)
    longest_streak = 0

    for num in s:
        if num - 1 not in s:  
            current_num = num
            current_streak = 1

            while current_num + 1 in s:  
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)  

    return longest_streak