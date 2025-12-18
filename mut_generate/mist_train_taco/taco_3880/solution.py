"""
QUESTION:
Mandarin chinese
, Russian and Vietnamese as well.
Let's denote $S(x)$ by the sum of prime numbers that divides $x$.
You are given an array $a_1, a_2, \ldots, a_n$ of $n$ numbers, find the number of pairs $i, j$ such that $i \neq j$, $a_i$ divides $a_j$ and $S(a_i)$ divides $S(a_j)$.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- First line of each testcase contains one integer $n$ — number of elements of the array.
- Second line of each testcase contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$.

-----Output:-----
For each testcase, output in a single line number of pairs that each of it satisfies given conditions.

-----Constraints-----
- $1 \leq T \leq 100$
- $2 \leq n, a_i \leq 10^6$
- the sum of $n$ for all test cases does not exceed $10^6$

-----Subtasks-----
Subtask #2 (20 points): $2 \leq n \leq 100$, $2 \leq a_i \leq 10^4$
Subtask #2 (80 points): original contsraints

-----Sample Input:-----
1
5
2 30 2 4 3

-----Sample Output:-----
6

-----EXPLANATION:-----
$S(2) = 2, S(30) = 2 + 3 + 5 = 10, S(4) = 2, S(3) = 3$. So using this information, the pairs of indicies are $(1,2)$, $(1, 3)$, $(1, 4)$, $(3, 1)$, $(3, 2)$, $(3, 4)$.
"""

def count_valid_pairs(test_cases):
    def prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors

    results = []
    
    for n, a in test_cases:
        s = [sum(prime_factors(x)) for x in a]
        count = 0
        for i in range(n):
            for j in range(n):
                if i != j and a[j] % a[i] == 0 and s[j] % s[i] == 0:
                    count += 1
        results.append(count)
    
    return results