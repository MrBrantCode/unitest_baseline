"""
QUESTION:
Given a sorted array of integers `numbers` and a target integer `target`, find two numbers that add up to `target`. Return the 1-indexed indices of these two numbers as an array of size 2, where `1 <= answer[0] < answer[1] <= numbers.length`. You may assume that each input has exactly one solution and that the same element cannot be used twice. The solution must be in-place and not use any additional data structures. 

Constraints: `2 <= numbers.length <= 3 * 10^4`, `-1000 <= numbers[i] <= 1000`, `numbers` is sorted in increasing order, and `-1000 <= target <= 1000`. Only one valid answer exists. The function should be named `two_sum` and take `numbers` and `target` as parameters.
"""

def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return [left + 1, right + 1]