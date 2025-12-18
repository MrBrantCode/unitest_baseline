"""
QUESTION:
Given a range L to R, the task is to find the highest occurring digit in prime numbers which lie between L and R (both inclusive). If multiple digits have same highest frequency return the largest of them. If no prime number occurs between L and R, return -1.
 
Example 1:
Input: L = 2, R = 10
Output: 7
Explanation: Between 2 and 10 every digit
has same frquency and 7 is largest among
them.
Example 2:
Input: L = 2, R = 20
Output: 1
Explanation: Prime number between 2 and 20 are 
2, 3, 5, 7, 11, 13, 17, 19. 1 occur 
maximum i.e 5 times among 0 to 9.
Your Task:  
You dont need to read input or print anything. Complete the function maxDigit() which takes L and R as input parameter and returns the highest occuring digit. If multiple digits have same highest frequency return the largest of them. If no prime number occurs between L and R, return -1.
Expected Time Complexity: O(nlog(n)sqrt(n))
Expected Auxiliary Space: O(k)
Constraints:
1 <= L<= R <= 1000
"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def highest_occurring_digit_in_primes(L, R):
    prime_digits = []
    
    for i in range(L, R + 1):
        if is_prime(i):
            c = i
            while c != 0:
                prime_digits.append(c % 10)
                c = c // 10
    
    if not prime_digits:
        return -1
    
    digit_count = {}
    for digit in prime_digits:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    
    max_count = 0
    max_digit = -1
    
    for digit, count in digit_count.items():
        if count > max_count or (count == max_count and digit > max_digit):
            max_count = count
            max_digit = digit
    
    return max_digit