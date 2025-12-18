"""
QUESTION:
Create a function called `proper_gcd` that takes two lists of unique integers as input and returns the highest shared factor (GCD) between any pair of numbers from the two lists. The lists are not sorted and their sizes are not predetermined. The function should correctly calculate the GCD for each pair of numbers and return the maximum GCD found.
"""

def proper_gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def find_highest_shared_factor(list1, list2):
    result_gcd = []
    for i in list1:
        for j in list2:
            result_gcd.append(proper_gcd(i, j))
    return max(result_gcd)