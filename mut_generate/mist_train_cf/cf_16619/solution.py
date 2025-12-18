"""
QUESTION:
Create a function named `increment_by_one` that increments a given integer by 1 using only bitwise operations. The function should have a time complexity of O(1) and cannot use any arithmetic operations, loops, or conditional statements. The function should work for both positive and negative integers.
"""

def increment_by_one(num):
    return -(-num & -~num)