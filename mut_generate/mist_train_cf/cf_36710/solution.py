"""
QUESTION:
Write a function `final_value(s, k)` that takes a string `s` consisting of lowercase English letters and an integer `k` as input. The function should perform the following operations `k` times: convert each character in `s` to its corresponding position in the alphabet (a=1, b=2, ..., z=26) and concatenate these values to form a new string `nums`, then replace the value of `nums` with the sum of its digits. The function should return the final value of `nums` as an integer.

Constraints: 
- 1 <= |s| <= 10^5 
- 1 <= k <= 10^9
"""

def final_value(s: str, k: int) -> int:
    nums = ''.join(str(ord(char) - ord('a') + 1) for char in s)
    for _ in range(k):
        nums = str(sum(int(c) for c in nums))
    return int(nums)