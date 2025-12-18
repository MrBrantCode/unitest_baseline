"""
QUESTION:
Your program fails again. This time it gets "Wrong answer on test 233".

This is the easier version of the problem. In this version $1 \le n \le 2000$. You can hack this problem only if you solve and lock both problems.

The problem is about a test containing $n$ one-choice-questions. Each of the questions contains $k$ options, and only one of them is correct. The answer to the $i$-th question is $h_{i}$, and if your answer of the question $i$ is $h_{i}$, you earn $1$ point, otherwise, you earn $0$ points for this question. The values $h_1, h_2, \dots, h_n$ are known to you in this problem.

However, you have a mistake in your program. It moves the answer clockwise! Consider all the $n$ answers are written in a circle. Due to the mistake in your program, they are shifted by one cyclically.

Formally, the mistake moves the answer for the question $i$ to the question $i \bmod n + 1$. So it moves the answer for the question $1$ to question $2$, the answer for the question $2$ to the question $3$, ..., the answer for the question $n$ to the question $1$.

We call all the $n$ answers together an answer suit. There are $k^n$ possible answer suits in total.

You're wondering, how many answer suits satisfy the following condition: after moving clockwise by $1$, the total number of points of the new answer suit is strictly larger than the number of points of the old one. You need to find the answer modulo $998\,244\,353$.

For example, if $n = 5$, and your answer suit is $a=[1,2,3,4,5]$, it will submitted as $a'=[5,1,2,3,4]$ because of a mistake. If the correct answer suit is $h=[5,2,2,3,4]$, the answer suit $a$ earns $1$ point and the answer suite $a'$ earns $4$ points. Since $4 > 1$, the answer suit $a=[1,2,3,4,5]$ should be counted.


-----Input-----

The first line contains two integers $n$, $k$ ($1 \le n \le 2000$, $1 \le k \le 10^9$) — the number of questions and the number of possible answers to each question.

The following line contains $n$ integers $h_1, h_2, \dots, h_n$, ($1 \le h_{i} \le k)$ — answers to the questions.


-----Output-----

Output one integer: the number of answers suits satisfying the given condition, modulo $998\,244\,353$.


-----Examples-----
Input
3 3
1 3 1

Output
9

Input
5 5
1 1 4 2 2

Output
1000



-----Note-----

For the first example, valid answer suits are $[2,1,1], [2,1,2], [2,1,3], [3,1,1], [3,1,2], [3,1,3], [3,2,1], [3,2,2], [3,2,3]$.
"""

def count_valid_answer_suits(n, k, h):
    M = 998244353
    
    # Calculate the number of mismatches when answers are shifted clockwise
    m = sum((i != j for (i, j) in zip(h, h[1:] + h[:1])))
    
    # Precompute factorials and their modular inverses
    f = [0] * (m + 1)
    f[0] = b = 1
    for i in range(1, m + 1):
        f[i] = b = b * i % M
    
    inv = [0] * (m + 1)
    inv[m] = b = pow(f[m], M - 2, M)
    for i in range(m, 0, -1):
        inv[i - 1] = b = b * i % M
    
    # Combination function
    comb = lambda n, k: f[n] * inv[n - k] * inv[k] % M
    
    # Calculate the final result
    result = (pow(k, m, M) - sum((comb(m, i) * comb(m - i, i) * pow(k - 2, m - i - i, M) for i in range(m // 2 + 1)))) * pow(k, n - m, M) * pow(2, M - 2, M) % M
    
    return result