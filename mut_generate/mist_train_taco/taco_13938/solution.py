"""
QUESTION:
There is a given string S consisting of N symbols. Your task is to find the number of ordered pairs of integers i and j such that

1. 1 ≤ i, j ≤ N

2. S[i] = S[j], that is the i-th symbol of string S is equal to the j-th.

Input

The single input line contains S, consisting of lowercase Latin letters and digits. It is guaranteed that string S in not empty and its length does not exceed 105.

Output

Print a single number which represents the number of pairs i and j with the needed property. Pairs (x, y) and (y, x) should be considered different, i.e. the ordered pairs count.

Examples

Input

great10


Output

7


Input

aaaaaaaaaa


Output

100
"""

def count_ordered_pairs(S: str) -> int:
    # Dictionary to store the frequency of each character
    char_count = {}
    
    # Count the frequency of each character in the string
    for char in S:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Calculate the number of ordered pairs for each character
    total_pairs = 0
    for count in char_count.values():
        total_pairs += count * count
    
    return total_pairs