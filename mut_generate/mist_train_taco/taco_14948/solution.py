"""
QUESTION:
A bracket sequence is a string, containing only characters "(", ")", "[" and "]".

A correct bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters "1" and "+" between the original characters of the sequence. For example, bracket sequences "()[]", "([])" are correct (the resulting expressions are: "(1)+[1]", "([1+1]+1)"), and "](" and "[" are not. The empty string is a correct bracket sequence by definition.

A substring s[l... r] (1 ≤ l ≤ r ≤ |s|) of string s = s1s2... s|s| (where |s| is the length of string s) is the string slsl + 1... sr. The empty string is a substring of any string by definition.

You are given a bracket sequence, not necessarily correct. Find its substring which is a correct bracket sequence and contains as many opening square brackets «[» as possible.

Input

The first and the only line contains the bracket sequence as a string, consisting only of characters "(", ")", "[" and "]". It is guaranteed that the string is non-empty and its length doesn't exceed 105 characters.

Output

In the first line print a single integer — the number of brackets «[» in the required bracket sequence. In the second line print the optimal sequence. If there are more than one optimal solutions print any of them.

Examples

Input

([])


Output

1
([])


Input

(((


Output

0
"""

def find_max_correct_bracket_sequence(bracket_sequence: str) -> (int, str):
    st, v, vi, vj, vc = [], [], 0, 0, 0
    
    for i, c in enumerate(bracket_sequence):
        if c in '[(':
            st.append(i)
            continue
        if st and bracket_sequence[st[-1]] + c in ('()', '[]'):
            b = (st[-1], i + 1)
            if v and v[-1][1] == i:
                v[-1] = b
            else:
                v.append(b)
            if len(v) >= 2 and v[-2][1] == v[-1][0]:
                v[-2:] = [(v[-2][0], v[-1][1])]
            st.pop()
        else:
            st = []
    
    for b in v:
        c = bracket_sequence.count('[', b[0], b[1])
        if c > vc:
            vi, vj, vc = b[0], b[1], c
    
    return vc, bracket_sequence[vi:vj]