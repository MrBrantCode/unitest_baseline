"""
QUESTION:
A string is called a k-string if it can be represented as k concatenated copies of some string. For example, the string "aabaabaabaab" is at the same time a 1-string, a 2-string and a 4-string, but it is not a 3-string, a 5-string, or a 6-string and so on. Obviously any string is a 1-string.

You are given a string s, consisting of lowercase English letters and a positive integer k. Your task is to reorder the letters in the string s in such a way that the resulting string is a k-string.

Input

The first input line contains integer k (1 ≤ k ≤ 1000). The second line contains s, all characters in s are lowercase English letters. The string length s satisfies the inequality 1 ≤ |s| ≤ 1000, where |s| is the length of string s.

Output

Rearrange the letters in string s in such a way that the result is a k-string. Print the result on a single output line. If there are multiple solutions, print any of them.

If the solution doesn't exist, print "-1" (without quotes).

Examples

Input

2
aazz


Output

azaz


Input

3
abcabcabz


Output

-1
"""

from collections import Counter

def reorder_to_k_string(k, s):
    # Create a frequency dictionary of characters in the string s
    char_count = Counter(s)
    
    # Initialize the result string
    result = ''
    
    # Check if each character count is divisible by k
    for char in char_count:
        if char_count[char] % k != 0:
            return -1
        else:
            # Append the character repeated (count // k) times to the result
            result += char * (char_count[char] // k)
    
    # Repeat the result string k times to form the final k-string
    return result * k