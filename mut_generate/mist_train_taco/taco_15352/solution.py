"""
QUESTION:
Given a string composed of both lowercase and uppercase letters. Sort it in such a manner such that the uppercase and lowercase letter comes in an alternate manner but in sorted way.
Example 1:
Input:
S = bAwutndekWEdkd
Output: AbEdWddekkntuw
Explanation: letters A,E,W are sorted 
as well as letters b,d,d,d,e,k,k,n,t,u,w are 
sorted and both appears alternately in the 
string as far as possible.
Ã¢â¬â¹Example 2:
Input: 
S = AiBFR
Output: AiBFR
Explanation: letters A,B,F,R and sorted 
as well as letter i. 
User Task:
You don't need to read input or print anything. You just have to complete the function stringSort () which takes a string as input and returns the sorted string as described in the problem description.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1). 
Constraints:
1<=|S|<=1000
"""

def alternate_sorted_string(s: str) -> str:
    upper = ''
    lower = ''
    res = ''
    
    # Separate uppercase and lowercase letters
    for char in s:
        if char.isupper():
            upper += char
        else:
            lower += char
    
    # Sort the uppercase and lowercase letters
    upper = sorted(upper)
    lower = sorted(lower)
    
    # Merge the sorted letters alternately
    if len(upper) < len(lower):
        for j in range(len(upper)):
            res += upper[j] + lower[j]
        for j in range(len(upper), len(lower)):
            res += lower[j]
    elif len(lower) < len(upper):
        for k in range(len(lower)):
            res += upper[k] + lower[k]
        for k in range(len(lower), len(upper)):
            res += upper[k]
    elif len(lower) == len(upper):
        for i in range(len(lower)):
            res += upper[i] + lower[i]
    
    return res