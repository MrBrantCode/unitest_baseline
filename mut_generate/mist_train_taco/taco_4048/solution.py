"""
QUESTION:
Given a number N. The task is to check if N is woodall number or not. A Woodall Number is of the form:
W_{n} = n.2^{n} – 1
The first few Woodall numbers are: 1, 7, 23, 63, 159, 383, 895……
Example 1:
Input: N = 383
Output: 1
Explaination: 6*2^{6} - 1 = 383.
Example 2:
Input: N = 200
Output: 0
Explaination: This is not a Woodall number.
Your task:
You do not need to read input or print anything. Your task is to complete the function isWoodall() which takes N as input parameter and returns 1 if it is a Woodall number, else returns 0.
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{6}
"""

def is_woodall(N):
    tem, c = N + 1, 0
    while tem % 2 == 0 and c < tem:
        tem = tem // 2
        c += 1
    if c == tem:
        return 1
    return 0