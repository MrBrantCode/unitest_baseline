"""
QUESTION:
Announcement
************Second Round will be ONLINE instead of ONSITE*************
Problem Statement

Schimdt is teaching Jenko a new technique to excel at bases. He writes n numbers in base k on a piece of paper and also their decimal sum. He doesn’t mention k on the paper. Jenko has to find out the value of k using those numbers and their sum. As Jenko is weak in maths, he needs your help to find the value of k.

Input

First line contains n, the count of numbers written on the paper. Next n lines contains the numbers in base k. Next line contains their decimal sum.

Output

Output the desired value of k. If multiple solutions are possible, print the minimum possible value.

Constraints

1 ≤ n ≤ 100000

2 ≤ k ≤ 16

Note: The decimal sum of all the numbers will never exceeds 10^18.

SAMPLE INPUT
2
10 21
10

SAMPLE OUTPUT
3

Explanation

10 in base 3=3 in base 10.
21 in base 3=7 in base 10.
Their sum is 3+7=10 which is given. So, 3 is the required answer
"""

def find_base_k(numbers, decimal_sum):
    # Determine the maximum digit in the numbers
    max_digit = 0
    for number in numbers:
        for digit in number:
            if digit.isalpha():
                digit_value = ord(digit.upper()) - ord('A') + 10
            else:
                digit_value = int(digit)
            if digit_value > max_digit:
                max_digit = digit_value
    
    # The minimum possible base is the maximum digit + 1, but at least 2
    min_base = max(2, max_digit + 1)
    
    # Check bases from min_base to 16
    for k in range(min_base, 17):
        sum_in_base_k = 0
        for number in numbers:
            sum_in_base_k += int(number, k)
        if sum_in_base_k == decimal_sum:
            return k
    
    # If no base is found, return -1
    return -1