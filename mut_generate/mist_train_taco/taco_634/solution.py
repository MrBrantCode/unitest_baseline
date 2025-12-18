"""
QUESTION:
Peter wrote on the board a strictly increasing sequence of positive integers a_1, a_2, ..., a_{n}. Then Vasil replaced some digits in the numbers of this sequence by question marks. Thus, each question mark corresponds to exactly one lost digit.

Restore the the original sequence knowing digits remaining on the board.


-----Input-----

The first line of the input contains integer n (1 ≤ n ≤ 10^5) — the length of the sequence. Next n lines contain one element of the sequence each. Each element consists only of digits and question marks. No element starts from digit 0. Each element has length from 1 to 8 characters, inclusive.


-----Output-----

If the answer exists, print in the first line "YES" (without the quotes). Next n lines must contain the sequence of positive integers — a possible variant of Peter's sequence. The found sequence must be strictly increasing, it must be transformed from the given one by replacing each question mark by a single digit. All numbers on the resulting sequence must be written without leading zeroes. If there are multiple solutions, print any of them.

If there is no answer, print a single line "NO" (without the quotes).


-----Examples-----
Input
3
?
18
1?

Output
YES
1
18
19

Input
2
??
?

Output
NO

Input
5
12224
12??5
12226
?0000
?00000

Output
YES
12224
12225
12226
20000
100000
"""

def restore_sequence(n, sequence):
    def solve(s, t, i, l):
        if i == l:
            return False
        if s[i] == '?':
            if solve(s, t, i + 1, l):
                s[i] = t[i]
                return True
            elif t[i] == '9':
                return False
            s[i] = nxt[t[i]]
            for j in range(i, l):
                if s[j] == '?':
                    s[j] = '0'
            return True
        elif s[i] > t[i]:
            for j in range(i, l):
                if s[j] == '?':
                    s[j] = '0'
            return True
        elif s[i] < t[i]:
            return False
        else:
            return solve(s, t, i + 1, l)

    a = [list(elem) for elem in sequence]
    p = ['0']
    nxt = {str(x): str(x + 1) for x in range(9)}
    
    for i, ai in enumerate(a):
        if len(p) > len(ai):
            return ("NO", None)
        if len(p) < len(ai):
            if a[i][0] == '?':
                a[i][0] = '1'
            for j in range(len(ai)):
                if a[i][j] == '?':
                    a[i][j] = '0'
        elif not solve(a[i], p, 0, len(ai)):
            return ("NO", None)
        p = a[i]
    
    restored_sequence = [int(''.join(line)) for line in a]
    return ("YES", restored_sequence)