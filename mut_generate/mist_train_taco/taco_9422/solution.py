"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Little Churu is a naughty child, who likes to play with balls. He has N buckets. Each bucket contains one or more balls. He has numbered his buckets 1 to N (both inclusive). He has an infinite supply of extra balls, apart from the ones already in the buckets. He wants to add zero or more number of balls to each of the buckets in such a way, that number of balls in the buckets are in a non-decreasing order, and their GCD is strictly greater than 1.

He wants to do it using the minimum number of extra balls. As he is too young to solve the problem, please help him with the solution.

------ Input ------ 

First line of input contains an integer T denoting the number of test cases.
For each test case, first line contains an integer N denoting the number of buckets.
Second line of each test case contains N space separated integers, where the i^{th} denotes the number of balls in the i^{th} bucket.

------ Output ------ 

For each test case, output a line containing a single integer — the answer for that test case.

------ Constraints ------ 

Subtask #1: 20 points

	$1 ≤ T  ≤ 10, 1 ≤ N  ≤ 1000, 1 ≤ number of balls in a bucket  ≤ 1000$

Subtask #2: 80 points

	$1 ≤ T  ≤ 10, 1 ≤ N  ≤ 10000, 1 ≤ number of balls in a bucket  ≤ 10000$

----- Sample Input 1 ------ 
1

3

11 13 15
----- Sample Output 1 ------ 
3
----- explanation 1 ------ 

Add one ball to each of the buckets.
"""

def min_extra_balls(buckets):
    def sieve():
        prime = [True] * 10003
        primes = []
        for i in range(2, 10003):
            if prime[i]:
                for j in range(i * i, 10003, i):
                    prime[j] = False
                primes.append(i)
        return primes

    primes = sieve()
    n = len(buckets)
    count = 0

    # Ensure the buckets are in non-decreasing order
    for i in range(1, n):
        if buckets[i] < buckets[i - 1]:
            count += buckets[i - 1] - buckets[i]
            buckets[i] = buckets[i - 1]

    ans = 10 ** 9
    for prime in primes:
        if prime > buckets[-1]:
            break
        required = 0
        tempans = count
        for j in buckets:
            if required < j:
                required = (j + prime - 1) // prime * prime
            tempans += required - j
            if tempans > ans:
                break
        if ans > tempans:
            ans = tempans

    return ans if buckets[-1] >= 2 else n