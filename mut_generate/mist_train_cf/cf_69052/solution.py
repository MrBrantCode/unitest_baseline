"""
QUESTION:
Create a function named `count_palindromic_numbers` to count the number of palindromic numbers nested within a given positive integer. The function should take one argument `n`, a significant positive integer, and return the count of palindromic numbers found. The function should consider single-digit numbers as palindromes.
"""

def count_palindromic_numbers(n):
    str_n = str(n)
    length = len(str_n)
    count = 0

    for i in range(length):
        for j in range(i + 1, length + 1):
            sub_num = str_n[i:j]
            if sub_num == sub_num[::-1]:
                count += 1
    return count