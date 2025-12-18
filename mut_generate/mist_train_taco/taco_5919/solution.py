"""
QUESTION:
Given a number n, find the ordered prime signatures and find the number of divisor of n.Any positive integer, ‘n’ can be expressed in the form of its prime factors. If ‘n’ has p_{1}, p_{2},  etc. as its prime factors, then n can be expressed as :
Arrange the obtained exponents of the prime factors of ‘n’ in non-decreasing order. The arrangement thus obtained is called the ordered prime signature of the positive integer ‘n’.
Example 1:
Input: n = 20
Output: 1 2
        6
Explaination: 20 can be written as 2^{2} * 5. The 
ordered pair is 2 1 and the factors are 1, 2, 4, 
5, 10, 20.
Example 2:
Input: n = 13
Output: 1
        2
Explaination: 13 itself is a prime number 
and it has two factors 1 and 13.
Your Task:
You do not need to read input or print anything. Your task is to complete the function orderedPrime() which takes n as input parameter and returns a list containing the powers in non-decreasing manner and the number of factors at the end of the list. The driver code will itself print the number of factors (last element of the returned list) in a new line.
Expected Time Complexity: O(nsqrt(n))
Expected Auxiliary Space: O(n)
Constraints:
2 ≤ n ≤ 10^{6}
"""

def ordered_prime_signature(n: int) -> list:
    def is_prime(N: int) -> bool:
        if N == 1:
            return False
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                return False
        return True

    prime_exponents = []
    divisor_count = 0
    current_exponent = 0

    for i in range(1, n + 1):
        if n % i == 0:
            divisor_count += 1
            if is_prime(i):
                d = n
                while d % i == 0:
                    current_exponent += 1
                    d //= i
                prime_exponents.append(current_exponent)
                current_exponent = 0

    prime_exponents.sort()
    prime_exponents.append(divisor_count)
    return prime_exponents