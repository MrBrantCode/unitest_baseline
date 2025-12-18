"""
QUESTION:
Given a string S and you need to check whether S contains two non overlapping substrings "XY" and "YX" in any order or not.
Note : All letters of the String are Uppercased.
 
Example 1:
Input:
S = "XYYX"
Output:
YES
Explanation: 
From stated input string "XY"
substring(1,2) and "YX" substring(3,4)
can be easily separated without overlap.
So output is "YES".
Example 2:
Input:
S = "XYX"
Output:
NO
Explanation: 
"XY" and "YX" substrings are present.
But they overlap with each other.
So, Output is "NO".
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function overlapPresent() which takes a String S and returns the answer.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= |S| <= 10^{5}
"""

def contains_non_overlapping_substrings(s: str) -> str:
    for i in range(1, len(s) - 1):
        left = s[0:i]
        right = s[i:len(s)]
        if ('XY' in left or 'YX' in left) and ('XY' in right or 'YX' in right):
            return 'YES'
    return 'NO'