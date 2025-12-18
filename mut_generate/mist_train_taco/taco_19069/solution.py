"""
QUESTION:
Problem Statement
As they say, small is cute and beautiful.

Given N distinct positive integers, find the smallest number that can be formed by concatenating all of them.
Input Format
The first line of the input file contains a positive integer N. Then N lines follow.
Each line contains a single positive integer K.

Output Format
Output the smallest possible number that can be formed by concatenating all the numbers.

Constraints
1 ≤ N ≤ 5000
1 ≤ K ≤ 10^15

SAMPLE INPUT
5
14
66
907
1234567890
9876543210

SAMPLE OUTPUT
123456789014669079876543210
"""

def find_smallest_concatenated_number(numbers):
    def custom_sort_key(a, b):
        str1 = a + b
        str2 = b + a
        if str1 > str2:
            return 1
        elif str1 == str2:
            return 0
        else:
            return -1
    
    numbers.sort(key=functools.cmp_to_key(custom_sort_key))
    return ''.join(numbers)