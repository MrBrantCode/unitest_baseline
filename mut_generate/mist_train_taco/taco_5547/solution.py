"""
QUESTION:
Mack gives Daisy two strings S1 and S2-consisting only of characters- 'M' and 'D' , and asks her to convert S1 to S2 in exactly N moves.

In a single move, Daisy has two choices:
Exchange any one 'M' with a 'D', or
Exchange any one 'D' with a 'M'.

You need to help Daisy if it's possible to transform S1 to S2 in exactly N moves. Output "Yes" if possible, else "No".

Input Format:
First line contains T, the number of test cases. T lines follow.
Each line consists of 2 space separated strings S1 and S2, and and the value N.

Output Format:
For each test case, print the answer, either "Yes" or "No"-(Without the quotes).

Constraints:
1 ≤ T ≤ 250
1 ≤ |S1|=|S2| ≤ 50
1 ≤ N ≤ 100

SAMPLE INPUT
3
MMDMDDM DDDDDDD 2
MMDD MMDD 1
MMMMMDMM DDDDDMDD 8

SAMPLE OUTPUT
No
No
Yes
"""

def can_transform_in_n_moves(s1: str, s2: str, n: int) -> str:
    # Calculate the number of differing positions between s1 and s2
    cnt = sum(1 for i in range(len(s1)) if s1[i] != s2[i])
    
    # Check if it's possible to transform s1 to s2 in exactly n moves
    if cnt <= n and (n - cnt) % 2 == 0:
        return "Yes"
    else:
        return "No"