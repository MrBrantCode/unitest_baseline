"""
QUESTION:
Given two strings, one is a text string and the other is a pattern string. The task is to print the indexes of all the occurrences of the pattern string in the text string. For printing, Starting Index of a string should be taken as 1.
Example 1:
Input:
S = "batmanandrobinarebat", pat = "bat"
Output: 1 18
Explanation: The string "bat" occurs twice
in S, one starts are index 1 and the other
at index 18. 
Example 2:
Input: 
S = "abesdu", pat = "edu"
Output: -1
Explanation: There's not substring "edu"
present in S.
Your Task:
You don't need to read input or print anything. Your task is to complete the function search() which takes the string S and the string pat as inputs and returns an array denoting the start indices (1-based) of substring pat in the string S. 
Note: You don't need to return -1 yourself when there are no possible answers, just return an empty list.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).
Constraints:
1 ≤ |S| ≤ 10^{5}
1 ≤ |pat| ≤ |S|
"""

def find_pattern_indices(text: str, pattern: str) -> list[int]:
    def z_function(s: str) -> list[int]:
        n = len(s)
        z = [0] * n
        (l, r) = (0, 0)
        for i in range(1, n):
            if i < r:
                z[i] = min(z[i - l], r - i)
            while z[i] + i < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                r = i + z[i]
                l = i
        return z

    combined = pattern + '$' + text
    z = z_function(combined)
    pattern_length = len(pattern)
    indices = []
    for i in range(pattern_length + 1, len(z)):
        if z[i] == pattern_length:
            indices.append(i - pattern_length)
    return indices