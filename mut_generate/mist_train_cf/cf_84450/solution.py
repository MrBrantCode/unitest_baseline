"""
QUESTION:
Write a function `check_substring_divisibility` that checks whether a given 10-digit pandigital number has the unique sub-string divisibility property, where the number is divisible by 4, 5, 6, 7, 8, 9, and 10 for the substrings of digits at positions 2-4, 3-5, 4-6, 5-7, 6-8, 7-9, and 8-10, respectively. The function should return True if the number has this property and False otherwise.
"""

def check_substring_divisibility(num):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return all(int(''.join(map(str,num[i+1:i+4]))) % divisors[i] == 0 for i in range(7))