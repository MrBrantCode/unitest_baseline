"""
QUESTION:
Given a number N, you need to find if its digital root is prime or not. DigitalRoot of a number is the repetitive sum of its digits until we get a single-digit number.
Eg.DigitalRoot(191)=1+9+1=>11=>1+1=>2
Example 1:
Input:
N = 89
Output:
0
Explanation:
DigitalRoot(89)=>17=>1+7=>8; not a prime.
Example 2:
Input:
N = 12
Output:
1
Explanation:
DigitalRoot(12)=>1+2=>3; a prime number.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function digitalRoot() which takes an integer N as an input parameter and return 1 if its digital root is a prime number otherwise return 0.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{4}
"""

def is_digital_root_prime(N: int) -> int:
    # Helper function to calculate the digital root
    def digital_root(num: int) -> int:
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num
    
    # Helper function to check if a number is prime
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
    
    # Calculate the digital root of N
    dr = digital_root(N)
    
    # Check if the digital root is prime
    if is_prime(dr):
        return 1
    else:
        return 0