"""
QUESTION:
Find all numbers in a list that are greater than a given number X and divisible by a given number Z.

Given a list of up to 10^6 integers ranging from -10^9 to 10^9, and two integers X and Z also ranging from -10^9 to 10^9, write a function `find_numbers_greater_and_divisible(lst, X, Z)` that returns a list of numbers from the input list that satisfy the conditions. The function should have a time complexity of O(N), where N is the length of the list, and use O(1) extra space excluding the output list.
"""

def find_numbers_greater_and_divisible(lst, X, Z):
    output = []
    for num in lst:
        if num > X and num % Z == 0:
            output.append(num)
    return output