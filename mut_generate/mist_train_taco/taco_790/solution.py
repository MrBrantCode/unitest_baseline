"""
QUESTION:
When you enter 8 numbers from 0 to 9, write a program that outputs the difference between the largest integer and the smallest integer that can sort the 8 numbers. The number that can be sorted may start from 0, such as 00135569.



Input

Given multiple datasets. The number of datasets n (n ≤ 50) is given on the first line. Then n rows of data are given. Each data is a sequence of 8 numbers (0 to 9 numbers).

Output

For each dataset, output the difference between the largest and smallest integers that can be rearranged in the entered numbers on one line.

Example

Input

2
65539010
65539010


Output

96417531
96417531
"""

def calculate_difference_of_sorted_numbers(numbers_list):
    results = []
    for c in numbers_list:
        sorted_desc = int(''.join(sorted(c, reverse=True)))
        sorted_asc = int(''.join(sorted(c)))
        results.append(sorted_desc - sorted_asc)
    return results