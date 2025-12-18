"""
QUESTION:
Given a string S, find the length of the longest substring without repeating characters. 
Example 1:
Input:
S = "geeksforgeeks"
Output:
7
Explanation:
Longest substring is
"eksforg".
Example 2:
Input:
S = "abdefgabef"
Output:
6
Explanation:
Longest substring are
"abdefg" , "bdefga" and "defgab".
 
Your Task:
You don't need to take input or print anything. Your task is to complete the function longestUniqueSubsttr() which takes a string S as and returns the length of the longest substring. 
 
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(K) where K is constant.
Constraints:
1 ≤ |S| ≤ 10^{5}
It is guaranteed that all characters of the String S will be lowercase letters from 'a' to 'z'
"""

def longest_unique_substring_length(S: str) -> int:
    seen = {}
    maximum_length = 0
    start = 0
    
    for end in range(len(S)):
        if S[end] in seen:
            start = max(start, seen[S[end]] + 1)
        seen[S[end]] = end
        maximum_length = max(maximum_length, end - start + 1)
    
    return maximum_length