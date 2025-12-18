"""
QUESTION:
The elections in which three candidates participated have recently ended. The first candidate received $a$ votes, the second one received $b$ votes, the third one received $c$ votes. For each candidate, solve the following problem: how many votes should be added to this candidate so that he wins the election (i.e. the number of votes for this candidate was strictly greater than the number of votes for any other candidate)?

Please note that for each candidate it is necessary to solve this problem independently, i.e. the added votes for any candidate do not affect the calculations when getting the answer for the other two candidates.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10^4$) — the number of test cases. Then $t$ test cases follow.

Each test case consists of one line containing three integers $a$, $b$, and $c$ ($0 \le a,b,c \le 10^9$).


-----Output-----

For each test case, output in a separate line three integers $A$, $B$, and $C$ ($A, B, C \ge 0$) separated by spaces — the answers to the problem for the first, second, and third candidate, respectively.


-----Examples-----

Input
5
0 0 0
10 75 15
13 13 17
1000 0 0
0 1000000000 0
Output
1 1 1
66 0 61
5 5 0
0 1001 1001
1000000001 0 1000000001


-----Note-----

None
"""

def calculate_votes_needed(a, b, c):
    def get_votes_needed(main, c1, c2):
        if main > c1 and main > c2:
            return 0
        x = max(c1, c2)
        ans = x - main + 1
        if main + ans > c1 and main + ans > c2:
            return ans
        if main + ans > c1:
            return ans + abs(main - c2 + 1)
        else:
            return ans + abs(main - c1 + 1)
    
    votes_needed_a = get_votes_needed(a, b, c)
    votes_needed_b = get_votes_needed(b, a, c)
    votes_needed_c = get_votes_needed(c, a, b)
    
    return (votes_needed_a, votes_needed_b, votes_needed_c)