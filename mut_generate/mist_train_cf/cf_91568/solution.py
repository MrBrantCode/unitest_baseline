"""
QUESTION:
Create a function called `count_pairs_divisible_by_3` that takes a list of integers as input and returns the count of pairs whose sum is divisible by 3. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def count_pairs_divisible_by_3(nums):
    count = 0
    remainder_count = [0, 0, 0]

    for num in nums:
        remainder = num % 3
        remainder_count[remainder] += 1

    count += (remainder_count[0] * (remainder_count[0] - 1)) // 2  
    count += remainder_count[1] * remainder_count[2]  

    return count