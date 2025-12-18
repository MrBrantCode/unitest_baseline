"""
QUESTION:
Alice and Bob are playing a game on a line with $n$ cells. There are $n$ cells labeled from $1$ through $n$. For each $i$ from $1$ to $n-1$, cells $i$ and $i+1$ are adjacent.

Alice initially has a token on some cell on the line, and Bob tries to guess where it is. 

Bob guesses a sequence of line cell numbers $x_1, x_2, \ldots, x_k$ in order. In the $i$-th question, Bob asks Alice if her token is currently on cell $x_i$. That is, Alice can answer either "YES" or "NO" to each Bob's question.

At most one time in this process, before or after answering a question, Alice is allowed to move her token from her current cell to some adjacent cell. Alice acted in such a way that she was able to answer "NO" to all of Bob's questions.

Note that Alice can even move her token before answering the first question or after answering the last question. Alice can also choose to not move at all.

You are given $n$ and Bob's questions $x_1, \ldots, x_k$. You would like to count the number of scenarios that let Alice answer "NO" to all of Bob's questions. 

Let $(a,b)$ denote a scenario where Alice starts at cell $a$ and ends at cell $b$. Two scenarios $(a_i, b_i)$ and $(a_j, b_j)$ are different if $a_i \neq a_j$ or $b_i \neq b_j$.


-----Input-----

The first line contains two integers $n$ and $k$ ($1 \leq n,k \leq 10^5$) — the number of cells and the number of questions Bob asked.

The second line contains $k$ integers $x_1, x_2, \ldots, x_k$ ($1 \leq x_i \leq n$) — Bob's questions.


-----Output-----

Print a single integer, the number of scenarios that let Alice answer "NO" to all of Bob's questions.


-----Examples-----
Input
5 3
5 1 4

Output
9

Input
4 8
1 2 3 4 4 3 2 1

Output
0

Input
100000 1
42

Output
299997



-----Note-----

The notation $(i,j)$ denotes a scenario where Alice starts at cell $i$ and ends at cell $j$.

In the first example, the valid scenarios are $(1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3), (3, 4), (4, 3), (4, 5)$. For example, $(3,4)$ is valid since Alice can start at cell $3$, stay there for the first three questions, then move to cell $4$ after the last question. 

$(4,5)$ is valid since Alice can start at cell $4$, stay there for the first question, the move to cell $5$ for the next two questions. Note that $(4,5)$ is only counted once, even though there are different questions that Alice can choose to do the move, but remember, we only count each pair of starting and ending positions once.

In the second example, Alice has no valid scenarios.

In the last example, all $(i,j)$ where $|i-j| \leq 1$ except for $(42, 42)$ are valid scenarios.
"""

def count_valid_scenarios(n, k, questions):
    # Initialize dictionaries to store the earliest and latest positions of each cell
    l = {i: k for i in range(n)}
    r = {i: -1 for i in range(n)}
    
    # Update the dictionaries based on Bob's questions
    for i, a in enumerate(questions):
        l[a - 1] = min(i, l[a - 1])
        r[a - 1] = max(i, r[a - 1])
    
    count = 0
    
    # Check all possible scenarios (a, b) where Alice starts at cell a and ends at cell b
    for i in range(n):
        for j in range(3):
            a = i
            b = i + j - 1
            if b < 0 or b >= n:
                continue
            if l[a] > r[b]:
                count += 1
    
    return count