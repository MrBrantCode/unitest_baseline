"""
QUESTION:
Given an integer N, you need to print the following pattern.
Example 1:
Input:
N = 3
Output:
33333
32223
32123
32223
33333
Explanation:
When N = 3 then there will be three boundaries.
Outer boundary contains only 3.
Middle boundary contains only 2.
And the inner boundary contains only 1.
Example 2:
Input:
N = 4
Output:
4444444
4333334
4322234
4321234
4322234
4333334
4444444
Your Task:  
You don't need to read input. Your task is to complete the function printPattern() which takes an integer N as an input parameter and print the pattern for it.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 9
"""

def generate_pattern(N):
    l = []
    for i in range(N, 0, -1):
        s = '' + str(N)
        k = N
        for j in range(0, N - i):
            k = k - 1
            s = s + str(k)
        s = s + (i - 1) * str(k)
        r = s[::-1]
        s = s + r[1:]
        l.append(s)
    l = l + l[::-1][1:]
    return l