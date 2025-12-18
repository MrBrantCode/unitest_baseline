"""
QUESTION:
Gru wanted to upgrade the quality of his minions' despicableness through his new base, The Volcano. Dave, desperately wanting the Minion of the Year award, rushed to The Volcano only to find out that he needs to solve a series of questions before he can unlock the gate and enter.

Dave is given a prime $\mbox{P}$, and $N$ questions.

In each question/query, Dave is given four integers $(A,B,C,D)$, and Dave needs to find the minimum possible value of $Ax+By$ among all positive integer pairs $(x,y)$ such that $\mbox{P}$ divides $|C^x-D^y|$.

Unfortunately, the gate has a strict time limit, and if Dave is unable to answer all questions quickly and correctly, then a hidden freeze ray will zap him and he won't be able to move. Please help Dave answer all the questions so he can enter The Volcano and win the Minion of the Year award!

Input Format 

The first line of input consists of an integer, $\mathbf{T}$, which is the number of test cases.

The first line of each test case consists of two integers separated by a space, $\mbox{P}$ and $N$. The following $N$ lines contain the queries, each in a line. Each question consists of four integers separated by single spaces: $\mbox{A}$, $\mbox{B}$, $\mbox{C}$ and $\mbox{D}$.

Output Format 

For each query, output a single line containing the minimum value of $Ax+By$, or output wala if no such pairs $(x,y)$ exist.

Constraints 

$1\leq T\leq3$ 

$1\leq N\leq6000$ 

$2\leq P\leq10^{8}$ 

$0\leq A,B,C,D\leq10^8$ 

$\mbox{P}$ is prime  

Sample Input  

2
7 2
1 1 1 5
7 8 8 7
11 5
1 1 1 1
0 1 2 3
3 2 1 0
9 8 7 6
0 0 1 1

Sample Output  

7
wala
2
1
wala
33
0

Explanation 

For the first query, $P=7$, $(A,B,C,D)=(1,1,1,5)$, the minimum $1x+1y$ is $7$, which occurs at $(x,y)=(1,6)$ ($7$ divides $\left|1^1-5^6\right|=15624=7\cdot2232$).

For the second query, no matter what $(x,y)$ you choose, $|8^x-7^y|$ will not by divisible by $7$, so the answer is wala.
"""

def min_value_for_queries(p, queries):
    results = []
    for [a, b, c, d] in queries:
        if c % p == 0:
            if d % p == 0:
                results.append(str(a + b))
            else:
                results.append('wala')
        elif d % p == 0:
            results.append('wala')
        else:
            toprint = (a + b) * p
            for x in range(1, p):
                for y in range(1, p):
                    if pow(c, x, p) == pow(d, y, p):
                        toprint = min(a * x + b * y, toprint)
            results.append(str(toprint))
    return results