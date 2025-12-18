"""
QUESTION:
Given an integer N, print an inverted isosceles triangle of stars such that the height of the triangle is N.
 
Example 1:
Input:
N = 4
Output:
*******
 *****
  ***
   *
Example 2:
Input:
N = 3
Output:
*****
 ***
  *
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function invIsoTriangle() which takes an Integer N as input and returns a vector of strings where each line represents lines of the pattern. For example, if N=2, the vector v = {"***", " * "}.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 100
"""

def generate_inverted_isosceles_triangle(N: int) -> list[str]:
    k = 0
    l = []
    s = N * 2 - 1
    for i in range(0, N):
        l.append(' ' * k + '*' * s)
        s = s - 2
        k = k + 1
    return l