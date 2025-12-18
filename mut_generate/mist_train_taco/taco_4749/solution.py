"""
QUESTION:
A prime number is a Circular Prime Number if all of its possible rotations are itself prime numbers. Now given a number N check if it is Circular Prime or Not.
 
Example 1:
Input: N = 197
Output: 1
Explanation: 197 is a Circular Prime because
all rotations of 197 are 197, 719, 971 all of 
the 3 are prime number's hence 197 is a 
circular prime.
Example 2:
Input: N = 101
Output: 0
Explanation: 101 and 11 is prime but 110 is
not a prime number.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function isCircularPrime() which takes N as input parameter and returns 1 if it is Circular Prime otherwise returns 0.
 
Expected Time Complexity: O(Nlog(log(N))
Expected Space Complexity: O(N)
 
Constraints:
1 <= N <= 10^{5}
"""

def is_circular_prime(n: int) -> int:
    def is_prime(x: int) -> bool:
        if x == 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    n_str = str(n)
    for i in range(len(n_str)):
        rotated = int(n_str[i:] + n_str[:i])
        if not is_prime(rotated):
            return 0
    return 1