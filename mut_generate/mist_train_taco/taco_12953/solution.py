"""
QUESTION:
Given a number N, find the maximum number of unique prime factors any number can have in range [1, N].
Example 1:
Input:
N = 3
Output:
1
Explanation:
No number in the range 1 to 3
can have more than 1 unique
Prime factor. So, the Output is 1.
Example 2:
Input:
N = 500
Output:
4
Explanation:
No number in the range 1 to 500
can have more than 4 unique
Prime factors. So, the Output is 4.
An example of a number with 4
unique Prime Factors is 210.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxUniquePrimeFactors() which takes an Integer N as input and returns the answer.
Expected Time Complexity: O(Largest Prime Factor of N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{18}
"""

def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    k = int(num ** 0.5)
    for i in range(2, k + 1):
        if num % i == 0:
            return False
    return True

def max_unique_prime_factors(N):
    """
    Function to find the maximum number of unique prime factors any number can have in the range [1, N].

    Parameters:
    N (int): The upper limit of the range [1, N].

    Returns:
    int: The maximum number of unique prime factors.
    """
    p = 1
    c = 0
    i = 2
    while p <= N:
        if is_prime(i):
            p = p * i
            if p <= N:
                c += 1
        i += 1
    return c