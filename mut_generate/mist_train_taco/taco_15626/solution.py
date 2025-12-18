"""
QUESTION:
Three guys play a game: first, each person writes down $n$ distinct words of length $3$. Then, they total up the number of points as follows:

if a word was written by one person — that person gets 3 points,

if a word was written by two people — each of the two gets 1 point,

if a word was written by all — nobody gets any points.

In the end, how many points does each player have?


-----Input-----

The input consists of multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 100$) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer $n$ ($1 \leq n \leq 1000$) — the number of words written by each person.

The following three lines each contain $n$ distinct strings — the words written by each person. Each string consists of $3$ lowercase English characters.


-----Output-----

For each test case, output three space-separated integers — the number of points each of the three guys earned. You should output the answers in the same order as the input; the $i$-th integer should be the number of points earned by the $i$-th guy.


-----Examples-----

Input
3
1
abc
def
abc
3
orz for qaq
qaq orz for
cod for ces
5
iat roc hem ica lly
bac ter iol ogi sts
bac roc lly iol iat
Output
1 3 1 
2 2 6 
9 11 5


-----Note-----

In the first test case:

The word ${abc}$ was written by the first and third guys — they each get $1$ point.

The word ${def}$ was written by the second guy only — he gets $3$ points.
"""

def calculate_points(test_cases):
    results = []
    
    for case in test_cases:
        n = case['n']
        P1 = set(case['words'][0])
        P2 = set(case['words'][1])
        P3 = set(case['words'][2])
        
        S1, S2, S3 = 0, 0, 0
        
        I = P1.intersection(P2, P3)
        P1.difference_update(I)
        P2.difference_update(I)
        P3.difference_update(I)
        
        I12 = P1.intersection(P2)
        I23 = P2.intersection(P3)
        I31 = P3.intersection(P1)
        
        S1 += len(I12) * 1 + len(I31) * 1
        S2 += len(I23) * 1 + len(I12) * 1
        S3 += len(I23) * 1 + len(I31) * 1
        
        P1.difference_update(I12)
        P2.difference_update(I12)
        P2.difference_update(I23)
        P3.difference_update(I23)
        P3.difference_update(I31)
        P1.difference_update(I31)
        
        S1 += len(P1) * 3
        S2 += len(P2) * 3
        S3 += len(P3) * 3
        
        results.append([S1, S2, S3])
    
    return results