"""
QUESTION:
In HackerLand, they have a very strange monetary system.
Each gold coin has an integer number 'N' written on it.
A coin N can be split into any number of coins.
For example {11} can be split into {5,6} or {2,4,5} or any other possible way.

You are offered such a coin to take home. But your family does not like coins which have a prime number on it. Your task is to take home as few coins as possible without a prime number on it.

Input:

The first line of the input contains a single integer T denoting the number of test cases to follow. Each test case is a single line with a number N. It is the number written on your coin. Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100,000  

Output:

For each test case output a single line, containing the minimum number of coins.

SAMPLE INPUT
4
11
12345
12421
2444

SAMPLE OUTPUT
2
1
2
1

Explanation

Test case 1:
{11} -> {1,10}. So, you can take home a possible minimum of 2 coins. NOTE: 1 is non-prime.

Test case 2:
{12345} can be taken home without splitting.
Similar for the rest of the test cases.
"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def split_coin(n, a):
    if not is_prime(n):
        a.append(n)
    else:
        c = 1
        n -= 1
        while is_prime(n):
            c += 1
            n -= 1
        a.append(n)
        split_coin(c, a)

def min_coins_without_primes(N):
    a = []
    split_coin(N, a)
    return len(a)