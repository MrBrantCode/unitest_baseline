"""
QUESTION:
February Easy Challenge 2015  is underway. Hackerearth welcomes you all and hope that all you awesome coders have a great time. So without wasting much of the time let's begin the contest.  

Prime Numbers have always been one of the favourite topics for problem setters. For more information on them you can use see this link http://en.wikipedia.org/wiki/Prime_number .  

Aishwarya is a mathematics student at the Department of Mathematics and Computing, California. Her teacher recently gave her an intriguing assignment with only a single question. The question was to find out the minimum number of single digit prime numbers which when summed equals a given number X. 

Input:
The first line contains T denoting the number of test cases. Each of the next T lines contains a single integer X.  

Output:
Print the minimum number required.  If it is not possible to obtain X using single digit prime numbers, output -1.  

Constraints:
1 ≤ T ≤ 100
1 ≤ X ≤ 10^6  

SAMPLE INPUT
4
7
10
14
11

SAMPLE OUTPUT
1
2
2
3

Explanation

10 can be represented as 7 + 3.

14 can be represented as 7+7

11 can be represented as 5+3+3.
"""

def minimum_primes_sum(X):
    # Single-digit prime numbers
    primes = [2, 3, 5, 7]
    
    # Dynamic programming array to store the minimum number of primes needed for each number up to X
    dp = [-1] * (X + 1)
    
    # Base cases
    dp[0] = 0  # 0 primes are needed to sum up to 0
    
    # Fill the dp array
    for i in range(1, X + 1):
        min_primes = float('inf')
        for prime in primes:
            if i >= prime and dp[i - prime] != -1:
                min_primes = min(min_primes, dp[i - prime] + 1)
        if min_primes != float('inf'):
            dp[i] = min_primes
    
    return dp[X]