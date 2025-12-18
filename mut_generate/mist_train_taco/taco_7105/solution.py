"""
QUESTION:
Once there was a Geek he was quite intelligent and was also fond of jumping. But he jumped in a pattern like 1 leap, 2 leap, 3 leap and again from the start after 3rd leap.
1 leap means if Geek is at point P then he will jump to P+1.
2 leap means if Geek is at point P then he will jump to P+2.
3 leap means if Geek is at point P then he will jump to P+3.
Find whether he could land up to a point N or not.
Note- He starts from point 0.
 
Example 1: 
Input: N = 0
Output: yes
Explanation:
Geek is already at Position 0.
Example 2: 
Input: N = 1
Output: yes
Explanation:
Geek will land at Position 1
after the 1st jump.
Example 3: 
Input: N = 8
Output: no
Explanation:
Geek can't land at Position 8.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function jumpingGeek() which takes an Integer N as input and returns "yes" if geek can reach N, otherwise return "no".
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
0 <= N <= 10^{8}
"""

def can_geek_land_at_position(N: int) -> str:
    k = N % 6
    if k == 0 or k == 1 or k == 3:
        return 'yes'
    else:
        return 'no'