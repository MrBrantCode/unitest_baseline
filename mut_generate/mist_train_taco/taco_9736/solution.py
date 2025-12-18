"""
QUESTION:
Greg wants to build a string, $\mbox{S}$ of length $N$. Starting with an empty string, he can perform $2$ operations:

Add a character to the end of $\mbox{S}$ for $\mbox{A}$ dollars.

Copy any substring of $\mbox{S}$, and then add it to the end of $\mbox{S}$ for $\mbox{B}$ dollars.

Calculate minimum amount of money Greg needs to build $\mbox{S}$.

Input Format

The first line contains number of testcases $\mathbf{T}$.        

The $2\times T$ subsequent lines each describe a test case over $2$ lines: 

The first contains $3$ space-separated integers, $N$, $\mbox{A}$ , and $\mbox{B}$, respectively. 

The second contains $\mbox{S}$ (the string Greg wishes to build).

Constraints

$1\leq T\leq3$
$1\leq N\leq3\times10^4$
$1\leq A,B\leq10000$
$\mbox{S}$ is composed of lowercase letters only.

Output Format

On a single line for each test case, print the minimum cost (as an integer) to build $\mbox{S}$.

Sample Input
2
9 4 5
aabaacaba
9 8 9
bacbacacb

Sample Output
26
42

Explanation

Test Case 0: 

$S_{initial}=$ ""; $S_{final}=$ "$aaba aaba$" 

Append "$a$"; $S=$ "$a$"; cost is $4$ 

Append "$a$"; $S=$ "$aa$"; cost is $4$ 

Append "$\boldsymbol{b}$"; $S=$ "$\textit{aab}$"; cost is $4$ 

Copy and append "$\boldsymbol{a}\boldsymbol{a}$"; $S=$ "$a abaa$"; cost is $5$ 

Append "$\textbf{C}$"; $S=$ "$a a b a c$"; cost is $4$ 

Copy and append "$\boldsymbol{aba}$"; $S=$ "$aaba aaba$"; cost is $5$        

Summing each cost, we get $4+4+4+5+4+5=26$, so our output for Test Case 1 is $26$.

Test Case 1: 

$S_{initial}=$ ""; $S_{final}=$ "$bacbacacb$" 

Append "$\boldsymbol{b}$"; $S=$ "$\boldsymbol{b}$"; cost is $8$ 

Append "$\boldsymbol{\alpha}$"; $S=$ "$\textbf{ba}$"; cost is $8$ 

Append "$\textbf{C}$"; $S=$ "$\textbf{bac}$"; cost is $8$ 

Copy and append "$\textbf{bac}$"; $S=$ "$bacbac$"; cost is $9$ 

Copy and append "$\boldsymbol{acb}$"; $S=$ "$bacbacacb$"; cost is $9$

Summing each cost, we get $8+8+8+9+9=42$, so our output for Test Case 2 is $\textbf{42}$.
"""

def calculate_minimum_cost(N, A, B, S):
    """
    Calculate the minimum cost to build the string S using the given operations.

    Parameters:
    - N (int): The length of the string S.
    - A (int): The cost to add a character to the end of S.
    - B (int): The cost to copy a substring and add it to the end of S.
    - S (str): The string Greg wishes to build.

    Returns:
    - int: The minimum cost to build the string S.
    """
    cost = [float('inf')] * (N + 1)
    cost[0] = 0
    k = 0
    for i in range(1, N + 1):
        j = max(i, k)
        while j <= N and S[i - 1:j] in S[:i - 1]:
            j += 1
        if j - 1 != i:
            cost[j - 1] = min(cost[i - 1] + B, cost[j - 1])
            k = j
        cost[i] = min(cost[i - 1] + A, cost[i])
    return cost[N]