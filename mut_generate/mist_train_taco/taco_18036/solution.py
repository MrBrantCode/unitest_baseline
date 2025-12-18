"""
QUESTION:
Given a string S, your task is to find the number of patterns of form 1[0]1 where [0] represents any number of zeroes (minimum requirement is one 0) there should not be any other character except 0 in the [0] sequence.
Example 1:
Input:
S = "100001abc101"
Output: 2
Explanation:
The two patterns are "100001" and "101".
Example 2:
Input:
S = "1001ab010abc01001"
Output: 2
Explanation:
The two patterns are "1001"(at start)
and "1001"(at end).
User Task:
Your task is to complete the function patternCount() which takes a single argument(string S) and returns the count of patterns. You need not take any input or print anything.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=Length of String<=10^5
"""

def count_patterns(S: str) -> int:
    length = len(S)
    count = 0
    i = 0
    
    while i < length - 1:
        if S[i] == '1' and i < length - 1:
            j = i + 1
            while j < length and S[j] == '0':
                j += 1
            if j < length and S[j] == '1':
                count += 1
            i = j
        else:
            i += 1
    
    return count