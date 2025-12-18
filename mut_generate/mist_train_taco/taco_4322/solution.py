"""
QUESTION:
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.


Example1:

a = 2
b = [3]

Result: 8



Example2:

a = 2
b = [1,0]

Result: 1024



Credits:Special thanks to @Stomach_ache for adding this problem and creating all test cases.
"""

def calculate_ab_mod_1337(a: int, b: list) -> int:
    result = 1
    fermatb = int(''.join(map(str, b))) % 570
    while fermatb:
        if fermatb & 1:
            result = result * a % 1337
        a = a * a % 1337
        fermatb >>= 1
    return result