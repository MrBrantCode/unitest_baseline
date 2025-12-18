"""
QUESTION:
A no is said to be  k-Almost Prime Number if it  has exactly k prime factors (not necessary distinct). Your task is to complete the function printKAlmostPrimes which takes two argument k and N and prints the  first N numbers that are k prime. 
Input:
The first line of input is the no of test cases . Then T test cases follow . Each test case contains two integers k and N .
Output:
For each test case output will be N space separated first N numbers that are k prime numbers.
Constraints:
1<=T<=100
1<=k<=10
1<=N<=50
Example(To be used only for expected output):
Input
1
2 5
Output
4 6 9 10 14
Explanation
In above test case
4 has two prime factors, 2 x 2
6 has two prime factors, 2 x 3
Similarly, 9(3 x 3), 10(2 x 5) and 14(2 x 7)
"""

def count_prime_factors(n):
    count = 0
    while n % 2 == 0:
        n = n // 2
        count += 1
    i = 3
    while i <= n ** 0.5:
        while n % i == 0:
            n //= i
            count += 1
        i += 2
    if n > 2:
        count += 1
    return count

def generate_k_almost_primes(k, N):
    result = []
    num = 2
    while len(result) < N:
        if count_prime_factors(num) == k:
            result.append(num)
        num += 1
    return result