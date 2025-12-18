"""
QUESTION:
Chef wants to gift pairs to his friends this new year. But his friends like good pairs
only.
A pair (a , b) is called a good pair if 1 <= a < b <= N such that GCD(a*b , P) = 1.
Since Chef is busy in preparation for the party, he wants your help to find all the
good pairs.
—————————————————————————————————————
INPUT
• The first line of the input contains a single integer T.
• The first and only line of each test case contain two integer N,P.
————————————————————————————————————————
OUTPUT
For each test case, print a single line containing one integer — the total number of good
pairs
————————————————————————————————————————
CONSTRAINTS
• 1 ≤ T≤ 50
• 2 ≤ N,P ≤10^5
—————————————————————————————————————
Example Input
2
2 3
3 3
————————————————————————————————————————
Example Output
1
1
"""

def count_good_pairs(N, P):
    def G(x, y):
        while y:
            (x, y) = (y, x % y)
        return x
    
    c = 0
    for i in range(1, N + 1):
        if G(i, P) == 1:
            c += 1
    
    ans = c * (c - 1) // 2
    return ans