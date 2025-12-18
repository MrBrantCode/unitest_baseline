"""
QUESTION:
Nikita has a row of $N$ white tiles indexed from $\mbox{1}$ to $N$. This time, she's painting them green! 

Find the number of ways Nikita can paint certain tiles in green so that the indices of the green tiles form an Arithmetic Progression. As this value can be quite large, your answer must be modulo $(10^9+7)$.

Note: Nikita must paint at least $\mbox{1}$ tile.

Input Format

The first line contains a single integer, $\mathbf{T}$, denoting the number of test cases. 

Each test case consists of a single line containing an integer, $N$, denoting the length of row of tiles.

Constraints

$1\leq T\leq10$
$1\leq N\leq10^{10}$

Scoring

$1\leq N\leq2000$ for $20\%$ of test data.
$1\leq N\leq10^5$ for $50\%$ of test data.
$1\leq N\leq10^{10}$ for $\textbf{100\%}$ of test data.

Output Format

On a new line for each test case, print the number of ways Nikita can paint her white tiles green so that the indices of the green tiles form an Arithmetic Progression. Because this number can be quite large, your answer must be modulo $(10^9+7)$.

Sample Input
3
3
4
5

Sample Output
7
13
22

Explanation

Test Case 0:

There are $7$ valid ways to paint the tiles:

Thus, we print the result of $7\%(10^9+7)$ on a new line, which is $7$.

Test Case 1:

There are $13$ valid ways to paint the tiles:

Thus, we print the result of $13\%(10^9+7)$ on a new line, which is $13$.
"""

def count_painting_ways(N, modo=10**9 + 7):
    def inv(n):
        return pow(n, modo - 2, modo)

    def faireNz(N, nz):
        raimax = (N - 1) // nz
        cb = nz - (N - 1) % nz - 1
        res = -cb * raimax + nz * (raimax * (raimax + 1) // 2)
        return res

    def arithm(db, nel, rai):
        return (rai * nel * (nel - 1) // 2 + db * nel) % modo

    rh, deb = N, N - 1
    tz = 1
    while True:
        nx = N // (tz + 1)
        nel, rai = deb - nx, (tz + 1) * tz // 2
        if nel < 4:
            break
        db = faireNz(N, deb)
        rh += arithm(db, nel, rai)
        deb, tz = nx, tz + 1

    for nz in range(1, deb + 1):
        rh = (rh + faireNz(N, nz)) % modo

    return rh