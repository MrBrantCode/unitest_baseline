"""
QUESTION:
Write a function named `generate_binary_strings` that takes an integer `N` as input and returns a list of all possible binary strings of length `N`. The function should not use any external libraries or input/output operations.
"""

def generate_binary_strings(N):
    if N == 0:
        return []
    if N == 1:
        return ['0', '1']
    result = []
    prev_strings = generate_binary_strings(N-1)
    for s in prev_strings:
        result.append(s + '0')
        result.append(s + '1')
    return result