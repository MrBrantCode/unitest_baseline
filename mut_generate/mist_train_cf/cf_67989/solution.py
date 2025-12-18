"""
QUESTION:
Write a function `longestRepeatingSubstring` that takes a string `S` as input and returns the length of the longest substring that repeats within `S`. If no repeating substring is present, return `0`. The string `S` consists only of lowercase English letters and its length is between `1` and `1500`.
"""

def longestRepeatingSubstring(S: str) -> int:
    n = len(S)
    nums = [ord(S[i]) - ord('a') for i in range(n)]
    a = 26  
    modulus = 2 ** 32  

    def search(L, a, modulus, n, nums):
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus
        
        seen = {h}
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        
        return -1

    left, right = 1, n
    while left < right:
        L = left + (right - left) // 2
        if search(L, a, modulus, n, nums) != -1:
            left = L + 1
        else:
            right = L

    return left - 1