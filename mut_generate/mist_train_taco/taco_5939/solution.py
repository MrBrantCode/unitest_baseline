"""
QUESTION:
You are given a string S consisting of lowercase English letters.
Another string T is initially empty.
Determine whether it is possible to obtain S = T by performing the following operation an arbitrary number of times:
 - Append one of the following at the end of T: dream, dreamer, erase and eraser.

-----Constraints-----
 - 1≦|S|≦10^5
 - S consists of lowercase English letters.

-----Input-----
The input is given from Standard Input in the following format:
S

-----Output-----
If it is possible to obtain S = T, print YES. Otherwise, print NO.

-----Sample Input-----
erasedream

-----Sample Output-----
YES

Append erase and dream at the end of T in this order, to obtain S = T.
"""

def can_form_string(S: str) -> str:
    # Reverse the input string
    S = ''.join(list(reversed(S)))
    
    # List of substrings to check, reversed
    str_list = ['dream', 'dreamer', 'erase', 'eraser']
    rev_str = [''.join(list(reversed(i))) for i in str_list]
    
    is_OK = True
    while len(S) > 0:
        if S[0:5] in rev_str:
            S = S[5:]
        elif S[0:6] in rev_str:
            S = S[6:]
        elif S[0:7] in rev_str:
            S = S[7:]
        else:
            is_OK = False
            break
    
    return 'YES' if is_OK else 'NO'