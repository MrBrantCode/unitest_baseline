"""
QUESTION:
Red John has committed another murder. This time, he doesn't leave a red smiley behind. Instead he leaves a puzzle for Patrick Jane to solve. He also texts Teresa Lisbon that if Patrick is successful, he will turn himself in. The puzzle begins as follows.  

There is a wall of size 4xn in the victim's house. The victim has an infinite supply of bricks of size 4x1 and 1x4 in her house. There is a hidden safe which can only be opened by a particular configuration of bricks. First we must calculate the total number of ways in which the bricks can be arranged so that the entire wall is covered.  The following diagram shows how bricks might be arranged to cover walls where $1\leq n\leq4$:

There is one more step to the puzzle.  Call the number of possible arrangements $\mbox{M}$.   Patrick must calculate the number of prime numbers $\mbox{P}$ in the inclusive range $\textbf{0}-M$.  

As an example, assume $n=3$.  From the diagram above, we determine that there is only one configuration that will cover the wall properly.  $\mbox{I}$ is not a prime number, so $P=0$.

A more complex example is $n=5$.  The bricks can be oriented in $3$ total configurations that cover the wall.  The two primes $2$ and $3$ are less than or equal to $3$, so $P=2$.

Function Description  

Complete the redJohn function in the editor below.  It should return the number of primes determined, as an integer.  

redJohn has the following parameter(s):  

n: an integer that denotes the length of the wall  

Input Format

The first line contains the integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases. 

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains an integer $n$, the length of the $4\times n$ wall.

Constraints

$1\leq t\leq20$
$1\leq n\leq40$

Output Format

Print the integer $\mbox{P}$ on a separate line for each test case.

Sample Input
2
1
7

Sample Output
0
3

Explanation

For $n=1$, the brick can be laid in 1 format only: vertically. 

The number of primes $\leq1$ is $\mbox{o}$. 

For $unrecognized$, one of the ways in which we can lay the bricks is 

There are $5$ ways of arranging the bricks for $n=7$ and there are $3$ primes $\leq5$.
"""

def redJohn(n):
    # Memoization for number of combinations
    nbCombMem = ([], [])

    def nbComb(N):
        if N in nbCombMem[0]:
            return nbCombMem[1][nbCombMem[0].index(N)]
        if N < 0:
            return 0
        c = 1
        for i in range(0, N - 3):
            c += nbComb(N - 4 - i)
        nbCombMem[0].append(N)
        nbCombMem[1].append(c)
        return c

    # Function to get primes under a given number
    def getPrimesUnder(n):
        r = [2]
        n2 = n // 2
        l = list((True for i in range(0, n2)))
        l[0] = False
        for i in range(1, n2):
            if l[i]:
                r.append(2 * i + 1)
                for m in range(2 * i * (i + 1), n2, 2 * i + 1):
                    l[m] = False
        return r

    # Calculate the number of ways to arrange the bricks
    M = nbComb(n)
    
    # Get the primes under M + 1
    primes = getPrimesUnder(M + 1)
    
    # Return the count of primes less than or equal to M
    return len(primes)