"""
QUESTION:
Ishaan has been given a task by his teacher. He needs to find the Nth term of a series. His teacher gives him some examples to help him out (Refer examples below). He is a bit weak in pattern searching so to help him his teacher told him that the Nth term is related to prime numbers. The Nth term is the difference of N and the closest prime number to N. Help him find the Nth term for a given N.
 
Example 1:
Input: N = 10
Output: 1
Explanation: Closest prime to 10 is 11.
Example 2:
Input: N = 7
Output: 0
Explanation: Closest prime to 7 is 7.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function NthTerm() which takes N as input paramater and returns Nth term.
 
Expected Time Complexity: O(N* √ N)
Expected Space Complexity: O(1)
Constraints:
1 <= N <= 100000
"""

def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def find_nth_term(N):
    if N == 1:
        return 1
    
    closest_prime_above = N
    while not is_prime(closest_prime_above):
        closest_prime_above += 1
    
    closest_prime_below = N
    while closest_prime_below > 1 and not is_prime(closest_prime_below):
        closest_prime_below -= 1
    
    if closest_prime_above - N > N - closest_prime_below:
        return N - closest_prime_below
    else:
        return closest_prime_above - N