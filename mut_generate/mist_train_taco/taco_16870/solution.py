"""
QUESTION:
Given a number N, find the number of binary strings of length N that contains consecutive 1's in them.
 
Example 1:
Input:
N = 2
Output:
1
Explanation:
There are 4 strings of 
length 2, the strings 
are 00, 01, 10, and 
11. Only the string 11 
has consecutive 1's.
 
 
Example 2:
Input:
N = 5
Output:
19
Explanation:
There are 19 strings
having consecutive 1's.
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numberOfConsecutiveOnes() which takes an integer N and returns the number of binary strings that contain consecutive 1's in them.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
 
Constraints
2 <= N <=30
"""

def numberOfConsecutiveOnes(N: int) -> int:
    (x, a, b) = (1, 0, 0)
    for i in range(N - 1):
        c = x + a + b
        (x, a, b) = (x << 1, c, a)
    return c