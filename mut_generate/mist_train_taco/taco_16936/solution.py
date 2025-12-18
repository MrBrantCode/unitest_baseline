"""
QUESTION:
A prime number is Super Prime if it is a sum of two primes. Find all the Super Primes upto N
Example 1:
Input:
N = 5
Output: 1
Explanation: 5 = 2 + 3, 5 is the
only super prime
Example 2:
Input:
N = 10 
Output: 2
Explanation: 5 and 7 are super primes
Your Task:  
You don't need to read input or print anything. Your task is to complete the function superPrimes() which takes the N as input and returns the count of super primes.
Expected Time Complexity: O(Nlog(logN))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
"""

def count_super_primes(n: int) -> int:
    """
    Counts the number of super primes up to a given integer n.

    A prime number is considered a super prime if it can be expressed as the sum of two primes.

    Parameters:
    n (int): The upper limit up to which to find super primes.

    Returns:
    int: The count of super primes up to n.
    """
    if n < 5:
        return 0
    
    # Sieve of Eratosthenes to find all primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # Count super primes
    count = 0
    for i in range(5, n + 1):
        if is_prime[i] and is_prime[i - 2]:
            count += 1
    
    return count