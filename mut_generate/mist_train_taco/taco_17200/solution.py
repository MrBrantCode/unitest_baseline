"""
QUESTION:
A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
Follow Up: Can you optimize it to O(N)
 
Example 1:
Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity. 
Example 2:
Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.
Your Task:
You don't need to read input or print anything. Complete the function celebrity() which takes the matrix M and its size N as input parameters and returns the index of the celebrity. If no such celebrity is present, return -1.
Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)
Constraints:
2 <= N <= 3000
0 <= M[][] <= 1
"""

def find_celebrity(M, N):
    i = 0
    j = N - 1
    while i < j:
        if M[i][j] == 1:
            i += 1
        else:
            j -= 1
    count = 0
    count2 = 0
    for j in range(N):
        if i != j:
            count += M[j][i]
            count2 += M[i][j]
    if count2 == 0 and count == N - 1:
        return i
    return -1