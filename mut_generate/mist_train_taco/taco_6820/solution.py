"""
QUESTION:
During the hypnosis session, Nicholas suddenly remembered a positive integer $n$, which doesn't contain zeros in decimal notation.

Soon, when he returned home, he got curious: what is the maximum number of digits that can be removed from the number so that the number becomes not prime, that is, either composite or equal to one?

For some numbers doing so is impossible: for example, for number $53$ it's impossible to delete some of its digits to obtain a not prime integer. However, for all $n$ in the test cases of this problem, it's guaranteed that it's possible to delete some of their digits to obtain a not prime number.

Note that you cannot remove all the digits from the number.

A prime number is a number that has no divisors except one and itself. A composite is a number that has more than two divisors. $1$ is neither a prime nor a composite number.


-----Input-----

Each test contains multiple test cases.

The first line contains one positive integer $t$ ($1 \le t \le 10^3$), denoting the number of test cases. Description of the test cases follows.

The first line of each test case contains one positive integer $k$ ($1 \le k \le 50$) — the number of digits in the number.

The second line of each test case contains a positive integer $n$, which doesn't contain zeros in decimal notation ($10^{k-1} \le n < 10^{k}$). It is guaranteed that it is always possible to remove less than $k$ digits to make the number not prime.

It is guaranteed that the sum of $k$ over all test cases does not exceed $10^4$.


-----Output-----

For every test case, print two numbers in two lines. In the first line print the number of digits, that you have left in the number. In the second line print the digits left after all delitions.

If there are multiple solutions, print any.


-----Examples-----

Input
7
3
237
5
44444
3
221
2
35
3
773
1
4
30
626221626221626221626221626221
Output
2
27
1
4
1
1
2
35
2
77
1
4
1
6


-----Note-----

In the first test case, you can't delete $2$ digits from the number $237$, as all the numbers $2$, $3$, and $7$ are prime. However, you can delete $1$ digit, obtaining a number $27 = 3^3$.

In the second test case, you can delete all digits except one, as $4 = 2^2$ is a composite number.
"""

def find_non_prime_number(t, test_cases):
    results = []
    c = ['1', '4', '6', '8', '9']
    c2 = ['25', '27', '32', '35', '52', '57', '72', '75']
    
    for i in range(t):
        k, n = test_cases[i]
        if k == 1:
            results.append((1, n))
            continue
        
        found = False
        for x in c:
            if x in n:
                results.append((1, x))
                found = True
                break
        
        if found:
            continue
        
        results.append((2, None))  # Placeholder for the 2-digit result
        if k == 2:
            results[-1] = (2, n)
            continue
        
        if n.count('2') >= 2:
            results[-1] = (2, '22')
            continue
        elif n.count('3') >= 2:
            results[-1] = (2, '33')
            continue
        elif n.count('5') >= 2:
            results[-1] = (2, '55')
            continue
        elif n.count('7') >= 2:
            results[-1] = (2, '77')
            continue
        
        for x in c2:
            if x in n:
                results[-1] = (2, x)
                found = True
                break
        
        if found:
            continue
        
        results[-1] = (2, n[0] + n[2])
    
    return results