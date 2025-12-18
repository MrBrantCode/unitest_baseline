"""
QUESTION:
Consider the palindromic prime numbers(Numbers which are palindrome as well as prime).Let p be the product of non zero digits of a nth palindromic prime number.Let product of digits of a palindromic prime is multiplied by a number m to generate number q(q=p*m).Your task is simple; you have to find number of divisors of q.

INPUT:

First Line contains number of test cases t.
Second line contains two space separated numbers n and m.

OUTPUT:

Output each test case in new line number of divisors of q.

CONSTRAINTS:

t ≤ 10000
n ≤ 113
1 ≤ m ≤ 100

SAMPLE INPUT
1
2 1

SAMPLE OUTPUT
2

Explanation

2nd palindromic prime is 3 value of m is 1 so value of q is 3.Numbers of divisors of 3 is 2(1 and 3)
"""

def find_divisors_of_q(n, m):
    # List of palindromic prime numbers
    palindromic_primes = [1, 2, 3, 5, 7, 1, 1, 3, 5, 8, 9, 9, 45, 63, 72, 98, 245, 392, 441, 81, 162, 3, 5, 6, 3, 4, 16, 28, 32, 27, 72, 81, 48, 112, 100, 125, 36, 108, 180, 216, 196, 441, 64, 256, 243, 648, 729, 9, 18, 36, 63, 72, 9, 45, 108, 144, 405, 720, 1152, 225, 225, 675, 1575, 648, 1620, 882, 2205, 576, 576, 4032, 1458, 98, 245, 294, 147, 441, 392, 1372, 441, 882, 2646, 784, 5488, 6125, 5292, 10584, 7203, 9604, 21609, 12544, 21952, 25088, 11907, 23814, 35721, 567, 81, 729, 1458, 5103, 1296, 3888, 7776, 10368, 11664, 18225, 5832, 11664, 20412, 11907, 19845, 31752, 15552, 31104, 3]
    
    # Get the nth palindromic prime number
    palindromic_prime = palindromic_primes[n]
    
    # Calculate the product of non-zero digits of the palindromic prime
    p = 1
    for digit in str(palindromic_prime):
        if digit != '0':
            p *= int(digit)
    
    # Calculate q = p * m
    q = p * m
    
    # Function to find the number of divisors of a number
    def count_divisors(num):
        cnt, prod = 0, 1
        while num % 2 == 0 and num != 1:
            num //= 2
            cnt += 1
        if cnt != 0:
            prod *= (cnt + 1)
        
        from math import sqrt
        for i in range(3, int(sqrt(num)) + 1, 2):
            cnt = 0
            while num % i == 0 and num != 1:
                num //= i
                cnt += 1
            if cnt != 0:
                prod *= (cnt + 1)
        
        if num != 1:
            prod *= 2
        
        return prod
    
    # Return the number of divisors of q
    return count_divisors(q)