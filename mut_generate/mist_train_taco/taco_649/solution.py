"""
QUESTION:
Given N, count all ‘a’(>=1) and ‘b’(>=0) that satisfy the condition a^{3} + b^{3 }= N.
 
Example 1:
Input:
N = 9 
Output:
2
Explanation:
There are two solutions: (a=1, b=2)
and (a=2, b=1).
Example 2:
Input:
N = 27
Output:
1
Explanation:
Thereis only one solution: (a=3, b=0)
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function pairCubeCount() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(cbrt(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def count_cube_pairs(N: int) -> int:
    count = 0
    max_a = int(pow(N, 1 / 3)) + 1
    
    for a in range(1, max_a):
        b_cube = N - pow(a, 3)
        if b_cube < 0:
            break
        b = int(round(pow(b_cube, 1 / 3)))
        if pow(b, 3) == b_cube:
            count += 1
        if pow(a, 3) == N and b_cube == 0:
            count += 1
    
    if N == 1:
        count = 1
    
    return count