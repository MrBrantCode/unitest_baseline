"""
QUESTION:
Given a number N. Find if it can be expressed as sum of two prime numbers.
Example 1:
Input: N = 34
Output: "Yes" 
Explanation: 34 can be expressed as 
sum of two prime numbers.
Example 2:
Input: N = 23
Output: "No"
Explanation: 23 cannnot be expressed as
sum of two prime numbers. 
Your Task:  
You dont need to read input or print anything. Complete the function isSumOfTwo() which takes N as input parameter and returns "Yes" if can be expressed as sum of two prime numbers. else return "No".
Expected Time Complexity: O(N*sqrt(N))
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{5}
"""

def is_sum_of_two_primes(N: int) -> str:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if N <= 3:
        return "No"
    
    if N % 2 == 0:
        return "Yes"
    
    if is_prime(N - 2):
        return "Yes"
    
    return "No"