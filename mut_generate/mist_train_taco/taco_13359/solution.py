"""
QUESTION:
Check the given number is prime or not using JAVA regex.
Example 1:
Input: N = 5
Output: 1
Explanation: 5 is prime number.
Example 2:
Input: N = 10
Output: 0
Explanation: 10 is not prime number.
 
Your Task:
You don't need to read or print anyhting.  Your task is to complete the function isPrime() which takes N as input parameter and returns 1 if N is prime otherwise returns 0.
 
Expected Time Complexity: O(N/2)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10000
"""

def isPrime(N: int) -> int:
    if N == 1:
        return 0
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            return 0
    return 1