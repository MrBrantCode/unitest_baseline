"""
QUESTION:
Generate a function named `generate_binary_strings` that takes an integer `N` as input and returns a list of all possible binary strings of length `N` with an equal number of 0s and 1s. The function should return an empty list if `N` is odd, as it's impossible to have an equal number of 0s and 1s in an odd-length binary string.
"""

def generate_binary_strings(N):
    if N % 2 != 0:
        return []  # N must be even for equal number of 0s and 1s
    
    strings = []
    def backtrack(string, zeros_left, ones_left):
        if zeros_left == 0 and ones_left == 0:
            strings.append(string)
            return
        
        if zeros_left > 0:
            backtrack(string + "0", zeros_left - 1, ones_left)
        
        if ones_left > 0:
            backtrack(string + "1", zeros_left, ones_left - 1)

    backtrack("", N // 2, N // 2)
    return strings