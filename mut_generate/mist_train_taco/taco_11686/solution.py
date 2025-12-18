"""
QUESTION:
Given a string S, Find all the possible subsequences of the String in lexicographically-sorted order.
Example 1:
Input : str = "abc"
Output: a ab abc ac b bc c
Explanation : There are 7 subsequences that 
can be formed from abc.
Example 2:
Input: str = "aa"
Output: a a aa
Explanation : There are 3 subsequences that 
can be formed from aa.
Your Task:
You don't need to read input or print anything. Your task is to complete the function AllPossibleStrings() which takes S as the input parameter and returns a list of all possible subsequences (non-empty) that can be formed from S in lexicographically-sorted order.
Expected Time Complexity: O(n*2^{n}) where n is the length of the String
Expected Space Complexity: O(n * 2^{n})
 
Constraints: 
1 <= Length of String <= 16
"""

from itertools import combinations

def generate_subsequences(s: str) -> list[str]:
    subsequences = []
    for i in range(1, 2 ** len(s)):
        subsequence = ''
        for j in range(len(s)):
            if i & (1 << j):
                subsequence += s[j]
        subsequences.append(subsequence)
    return sorted(subsequences)