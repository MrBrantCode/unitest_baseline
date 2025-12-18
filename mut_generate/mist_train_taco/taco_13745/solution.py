"""
QUESTION:
Given N distinct digits in an array A (from 1 to 9), Your task is to complete the function getSum which finds sum of all n digit numbers that can be formed using these digits. 
Note: Since the output can be large take modulo 1000000007
Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains an integer N . In the next line are N space separated digits.
Output:
For each test case in a new line output will be the sum of all n digit numbers that can be formed using these digits.
Constraints:
1<=T<=100
1<=N<=9
Example(To be used only for expected output):
Input:
2
3
1 2 3
2
1 2
Output:
1332
33
Explanation:
For first test case
the numbers formed will be 123 , 132 , 312 , 213, 231 , 321
sum = 123 + 132 + 312 + 213 + 231 + 321 = 1332
For second test case
the numbers formed will be 12, 21
sum = 12 + 21 = 33
"""

from itertools import permutations

MOD = 10 ** 9 + 7

def calculate_sum_of_permutations(digits):
    # Convert each digit to a string
    str_digits = [str(digit) for digit in digits]
    
    # Initialize the sum
    total_sum = 0
    
    # Generate all permutations of the digits
    for perm in permutations(str_digits):
        # Convert the permutation tuple to an integer
        number = int(''.join(perm))
        # Add the number to the total sum
        total_sum += number
    
    # Return the sum modulo 1000000007
    return total_sum % MOD