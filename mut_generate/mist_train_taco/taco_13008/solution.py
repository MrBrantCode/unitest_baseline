"""
QUESTION:
Read problems statements in Mandarin Chinese . 

You are given two strings A and B of the same length. Each string contains N Lower case Latin character (from 'a' to 'z'). A shift operation will remove the first character of a string and add the same character at the end of that string. For example after you perform a shift operation on a string 'abcd', the new string will be 'bcda'. If you perform this operation two times, the new string will be 'cdab'. You need to use some (maybe none) shift operations on the string B to maximize the length of the longest common prefix of A and B. If more than one result can be found pick the one that use smallest number of shift operations.

------ Input ------ 

The first line of the input contains a single integer N. The second and the third lind contains the string A and B respectively.
 
------ Output ------ 

Contains a single integer which is the number of shift operations.
 
------ Constraints ------ 

30 points:
$1 ≤ N ≤ 5000$
30 points:
$1 ≤ N ≤ 10^{4}$
40 points:
$1 ≤ N ≤ 10^{6}$

----- Sample Input 1 ------ 
5
ccadd
bddcc
----- Sample Output 1 ------ 
3
"""

def find_max_prefix_shifts(N, A, B):
    B += B  # Concatenate B with itself to simulate shifts
    first = 0
    second = N - 1
    op = 0
    
    while first <= second:
        m = (first + second) // 2
        c = A[:m + 1]
        x = B.find(c)
        
        if x == -1:
            second = m - 1
        else:
            first = m + 1
        
        if op < x:
            op = x
    
    return op