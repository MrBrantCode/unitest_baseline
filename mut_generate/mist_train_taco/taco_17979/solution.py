"""
QUESTION:
Given a number N, calculate the prime numbers up to N using Sieve of Eratosthenes.  
Example 1:
Input:
N = 10
Output:
2 3 5 7
Explanation:
Prime numbers less than equal to N 
are 2 3 5 and 7.
Example 2:
Input:
N = 35
Output:
2 3 5 7 11 13 17 19 23 29 31
Explanation:
Prime numbers less than equal to 35 are
2 3 5 7 11 13 17 19 23 29 and 31.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sieveOfEratosthenes() which takes an integer N as an input parameter and return the list of prime numbers less than equal to N.
Expected Time Complexity: O(NloglogN)
Expected Auxiliary Space: O(N)
Constraints:
1<= N <= 10^{4}
"""

def sieve_of_eratosthenes(N):
    prime = [True] * (N + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, N + 1):
        if prime[i]:
            j = i * 2
            while j < N + 1:
                prime[j] = False
                j += i
    ans = []
    for p in range(N + 1):
        if prime[p]:
            ans.append(p)
    return ans