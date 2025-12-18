"""
QUESTION:
Minion's approach is Correct, if number of the positive integers less than or equal to N that are relatively prime to N, is prime or else Incorrect.
In other words, let Z be the number of integers K in the range 1 ≤ K ≤ N for which the greatest common divisor gcd(N,K) = 1. If Z is prime then Minion's Approach is Correct else it is Incorrect.

Given an integer N, your task is to check if a minions approach is Correct or Incorrect.

Input: First line contains T - number of test cases.
Each of next T lines contain an integer N.

Output: Print approach type of each N in a new line i.e. "Correct" or "Incorrect".

Constraints:   1 ≤ T ≤ 10   |   1 ≤ N ≤ 100000 

SAMPLE INPUT
4
2
3
4
5

SAMPLE OUTPUT
Incorrect
Correct
Correct
Incorrect

Explanation

For N=4, numbers ≤ 4 and relatively prime to 4 are 1 and 3. So there are 2 numbers that are relatively prime to 4. Since 2 is a prime. Approach is Correct.

For N=5, numbers ≤ 5 and relatively prime to 5 are 1,2,3 and 4. So there are 4 numbers that are relatively prime to 5. Since 4 is not a prime. Approach is Incorrect.
"""

from math import gcd, sqrt

def check_minion_approach(N):
    # Function to count the number of integers relatively prime to N
    def count_coprimes(N):
        count = 0
        for i in range(1, N + 1):
            if gcd(i, N) == 1:
                count += 1
        return count
    
    # Function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    # Count the number of integers relatively prime to N
    Z = count_coprimes(N)
    
    # Check if Z is prime
    if is_prime(Z):
        return "Correct"
    else:
        return "Incorrect"