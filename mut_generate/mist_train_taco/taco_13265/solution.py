"""
QUESTION:
Given two integers L and R, write a program that finds the count of numbers having prime number of set bits in their binary representation in the range [L, R].
Example 1:
Input: L = 6, R = 10
Output: 4
Explanation: 6, 7, 9, 10 having
prime set bits between 6 and 10. 
Example 2:
Input: L = 10, R = 15
Output: 5
Explanation: 10, 11, 12, 13, 14 having
prime set bits between 10 and 15.
Your Task:  
You dont need to read input or print anything. Complete the function primeSetBits() which takes L and R as input parameter and returns the count of numbers having prime number of set bits in their binary representation.
Expected Time Complexity: O(nlog(n)sqrt(n))
Expected Auxiliary Space: O(1)
Constraints:
1 <= L <= R <=1000
"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_numbers_with_prime_set_bits(L, R):
    count = 0
    for i in range(L, R + 1):
        set_bits_count = bin(i).count('1')
        if is_prime(set_bits_count):
            count += 1
    return count