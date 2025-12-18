"""
QUESTION:
A bracket sequence is a string that is one of the following:
 - An empty string;
 - The concatenation of (, A, and ) in this order, for some bracket sequence A ;
 - The concatenation of A and B in this order, for some non-empty bracket sequences A and B /
Given are N strings S_i. Can a bracket sequence be formed by concatenating all the N strings in some order?

-----Constraints-----
 - 1 \leq N \leq 10^6
 - The total length of the strings S_i is at most 10^6.
 - S_i is a non-empty string consisting of ( and ).

-----Input-----
Input is given from Standard Input in the following format:
N
S_1
:
S_N

-----Output-----
If a bracket sequence can be formed by concatenating all the N strings in some order, print Yes; otherwise, print No.

-----Sample Input-----
2
)
(()

-----Sample Output-----
Yes

Concatenating (() and ) in this order forms a bracket sequence.
"""

def can_form_bracket_sequence(n, strings):
    ls1 = []
    ls2 = []
    
    for item in strings:
        stk1 = []
        stk2 = []
        for ch in item:
            if ch == '(':
                stk2.append(ch)
            elif len(stk2) > 0:
                stk2.pop()
            else:
                stk1.append(ch)
        l1 = len(stk1)
        l2 = len(stk2)
        if l2 >= l1:
            ls1.append((l1, l2))
        else:
            ls2.append((l1, l2))
    
    ls1.sort()
    cnt = 0
    for item in ls1:
        cnt -= item[0]
        if cnt < 0:
            return False
        else:
            cnt += item[1]
    
    ls2.sort(key=lambda x: x[1])
    ls2.reverse()
    for item in ls2:
        cnt -= item[0]
        if cnt < 0:
            return False
        else:
            cnt += item[1]
    
    return cnt == 0