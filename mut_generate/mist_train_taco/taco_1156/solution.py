"""
QUESTION:
Given an array s containing n strings, find the length of the string obtained by combining the strings. Two strings can be only combined if the last character of the first string and the first character of the second string are the same.
Example 1:
Input:
n = 3
s[] = {"RBR", "BBR", "RRR"}
Output: 9
Explanation: Combined string can 
             be: BRR + RBR + RRR
Example 2:
Input:
n = 2
s[] = {"RRR", "BBB"}
Output: 0
Explanation: Since combining condition
             isn't fulfilled answer is 0.
Your Task:
Your task is to complete the function combine() which takes 2 arguments(integer n and array of n strings) and returns the maximum length of combined strings possible. If no 2 strings can be combined return 0. 
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
Constraints:
2<=n<=1000
1<=|s_{i}|<=1000, where 0<=i<n
s will only contain {R,B}
"""

def calculate_max_combined_length(n, s):
    BB = RR = BR = RB = 0
    for i in s:
        if i[0] + i[-1] == 'BB':
            BB += 1
        elif i[0] + i[-1] == 'RR':
            RR += 1
        elif i[0] + i[-1] == 'RB':
            RB += 1
        elif i[0] + i[-1] == 'BR':
            BR += 1
    
    mn = min(BR, RB)
    ans = 0
    
    if not BR and not RB:
        ans = max(BB, RR)
    elif RB == BR:
        ans = BB + RR + 2 * mn
    else:
        ans = BB + RR + 2 * mn + 1
    
    ans *= len(s[0])
    return 0 if ans == len(s[0]) else ans