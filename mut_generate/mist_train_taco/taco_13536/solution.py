"""
QUESTION:
Given a string s, the task is to check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.  
Example 1:
Input: s = "ababab"
Output: 1
Explanation: It is contructed by 
appending "ab" 3 times
Example 2:
Input: s = "ababac"
Output: 0
Explanation: Not possible to construct
User Task:
Your task is to complete the function isRepeat() which takes a single string as input and returns 1 if possible to construct, otherwise 0. You do not need to take any input or print anything.
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)
Constraints:
1 <= |s| <= 10^{5}
"""

def can_be_constructed_by_repeating_substring(s: str) -> int:
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s1 = s[:i]
            if s1 * (n // i) == s:
                return 1
    return 0