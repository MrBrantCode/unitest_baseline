"""
QUESTION:
Create a function `get_odd_cubic_roots` that takes a list of integers as input. Calculate the cubic root of each number in the list and verify if the cubic root is an odd number. If it is, store the original number and its cubic root in a dictionary with the original number as the key and the cubic root as the value. Ensure the cubic root checking function can handle negative numbers and zero. The function should have a time complexity of O(n), where n is the number of elements in the input list.
"""

def get_odd_cubic_roots(numbers):
    cubic_roots = {i: i**(1./3.) if i>=0 else -(-i)**(1./3.) for i in numbers}
    odd_cubic_roots = {i : cubic_roots[i] for i in cubic_roots if cubic_roots[i] % 2 == 1}
    return odd_cubic_roots