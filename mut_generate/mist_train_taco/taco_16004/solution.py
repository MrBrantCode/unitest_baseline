"""
QUESTION:
Given a string containing lower and uppercase alphabets, the task is to find the maximum number of characters between any two same (case sensitivity) character in the string. 
Example 1:
Input:
S = "socks"
Output: 3
Explanation: There are 3 characters between
the two occurrences of 's'.
Example 2:
Input: 
S = "FoR"
Output: -1
Explanation: No repeating character present.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxChars() which takes the string S as input and returns the maximum number of characters between any two same characters in the string.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
"""

def max_chars_between_same_characters(s: str) -> int:
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    mx = -1
    for key in d:
        if len(d[key]) > 1:
            t = d[key][-1] - d[key][0] - 1
            if t > mx:
                mx = t
    return mx