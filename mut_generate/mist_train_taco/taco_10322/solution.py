"""
QUESTION:
There are N dominoes in a line, and we place each domino vertically upright.
In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
Return a string representing the final state. 
Example 1:
Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Example 2:
Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
"""

def calculate_final_domino_state(dominoes: str) -> str:
    INF = float('inf')
    n = len(dominoes)
    d1 = [-1] * n
    d2 = [-1] * n
    cnt = INF
    
    # Calculate the distance to the nearest 'L' from the right
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            cnt = 0
        elif dominoes[i] == '.':
            cnt += 1
        elif dominoes[i] == 'R':
            cnt = INF
        d1[i] = cnt
    
    cnt = INF
    
    # Calculate the distance to the nearest 'R' from the left
    for i in range(n):
        if dominoes[i] == 'R':
            cnt = 0
        elif dominoes[i] == '.':
            cnt += 1
        elif dominoes[i] == 'L':
            cnt = INF
        d2[i] = cnt
    
    ret = []
    
    # Determine the final state of each domino
    for i in range(n):
        if d1[i] == d2[i]:
            ret.append('.')
        elif d1[i] < d2[i]:
            ret.append('L')
        else:
            ret.append('R')
    
    return ''.join(ret)