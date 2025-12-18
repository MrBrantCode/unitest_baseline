"""
QUESTION:
Given a string S, find the length of the longest substring with all distinct characters. 
Example 1:
Input:
S = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest 
substring with all distinct characters.
Example 2:
Input: 
S = "aaa"
Output: 1
Explanation: "a" is the longest substring 
with all distinct characters.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestSubstrDitinctChars() which takes the string S as input and returns the length of the longest substring with all distinct characters.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(K), where K is Constant.
Constraints:
1<=|S|<=10^{5}
"""

def longest_substring_with_distinct_chars(S: str) -> int:
    seen = {}
    maximum_length = 0
    start = 0
    
    for end in range(len(S)):
        if S[end] in seen:
            start = max(start, seen[S[end]] + 1)
        seen[S[end]] = end
        maximum_length = max(maximum_length, end - start + 1)
    
    return maximum_length