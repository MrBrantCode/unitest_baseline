"""
QUESTION:
Sarthak has a set S of N distinct prime numbers. He grew very fond of that set, and now he only likes a positive integer X if all of its prime factors belong to S. Given the set and a positive integer M, can you find out how many integers he likes which are not more than M?

Note: Sarthak always like the number 1.

------ Input Format ------ 

- The first line of each input contains T - the number of test cases. The test cases then follow.
- The first line of each test case contains two space-separated integers N and M - the size of S and the limit defined in the statement.
- The second line of each test case contains N space-separated integers S_{1}, S_{2}, \dots, S_{N} - the elements of S.

------ Output Format ------ 

For each test case, output on a single line the number of positive integers Sarthak likes that is not more than M. 

------ Constraints ------ 

$1 ≤ T ≤ 2$
$1 ≤ N ≤ 20$
$1 ≤ M ≤ 10^{16}$
$2 ≤ S_{i} < 1000$
$S$ has $N$ distinct prime numbers

----- Sample Input 1 ------ 
1
2 10
3 5

----- Sample Output 1 ------ 
4
----- explanation 1 ------ 
- Test case $1$: Sarthak likes the numbers $1$, $3$, $5$ and $9$.
"""

def count_liked_numbers(T, test_cases):
    results = []
    for case in test_cases:
        N, M, S = case
        primes = sorted(S)
        
        def calculate(primeset, m):
            valueset = [1]
            for x in primeset:
                i = 0
                while i < len(valueset):
                    if valueset[i] * x <= m:
                        valueset.append(valueset[i] * x)
                    i += 1
            return valueset
        
        primeset1 = [primes[i] for i in range(0, N, 2)]
        primeset2 = [primes[i] for i in range(1, N, 2)]
        valueset1 = calculate(primeset1, M)
        valueset2 = calculate(primeset2, M)
        valueset1.sort()
        valueset2.sort()
        
        ans = 0
        start, end = 0, len(valueset2) - 1
        while start < len(valueset1) and end >= 0:
            if valueset1[start] * valueset2[end] <= M:
                ans += end + 1
                start += 1
            else:
                end -= 1
        
        results.append(ans)
    
    return results