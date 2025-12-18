"""
QUESTION:
Given a string, find the number of pairs of characters that are same. Pairs (s[i], s[j]), (s[j], s[i]), (s[i], s[i]), (s[j], s[j]) should be considered different.
Example 1:
Input:
S = "air"
Output: 3
Explanation: 3 pairs that are equal:
(S[0], S[0]), (S[1], S[1]) and (S[2], S[2])
Ã¢â¬â¹Example 2:
Input: 
S = "aa"
Output: 4
Explanation: 4 pairs that are equal:
(S[0], S[0]), (S[0], S[1]), (S[1], S[0])
and (S[1], S[1])
Your Task:
You don't need to read input or print anything. Your task is to complete the function equalPairs() which takes the string S as input and returns the number of equal pairs as described in the problem description.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
"""

def count_equal_pairs(s: str) -> int:
    result = 0
    d = {}
    
    # Count the frequency of each character
    for char in s:
        d[char] = d.get(char, 0) + 1
    
    # Calculate the number of equal pairs
    for count in d.values():
        result += count * count
    
    return result