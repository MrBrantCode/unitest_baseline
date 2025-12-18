"""
QUESTION:
Write a function `sum_odd_no_multiples_of_3` that takes an integer `n` as input and returns the sum of all odd numbers up to `n` excluding any multiples of 3. Implement the solution using recursion with a space complexity of O(1) and a time complexity of O(n).
"""

def sum_odd_no_multiples_of_3(n, current_sum=0):
    if n == 0:
        return current_sum
    elif n % 3 == 0:
        return sum_odd_no_multiples_of_3(n-1, current_sum)
    elif n % 2 == 1:
        current_sum += n
    return sum_odd_no_multiples_of_3(n-1, current_sum)