"""
QUESTION:
For a given value N, denoting the number of Characters starting from the A, print reverse character bridge pattern.
 
Example 1:
Input:
N = 5
Output:
ABCDEDCBA
ABCD DCBA
ABC   CBA
AB     BA
A       A
Example 2:
Input:
N = 4
Output:
ABCDCBA
ABC CBA
AB   BA
A     A
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function revCharBridge() which takes an Integer N as input and returns a vector of strings where each line represents lines of the pattern. For example, if N = 3, the vector v = {"ABCBA", "AB BA", "A   A"}.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
2 <= N <= 26
"""

def revCharBridge(N):
    l = []
    co = 0
    c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(N, 0, -1):
        start = c[:i]
        if i == N - 1:
            co = 1
        else:
            co += 2
        center = ' ' * co
        end = start[::-1]
        if i == N:
            l.append(start + end[1:])
        else:
            l.append(start + center + end)
    return l