"""
QUESTION:
Write a recursive function `sum_odd_no_multiples_of_3` to calculate the sum of all odd numbers up to a given number `n`, excluding any multiples of 3. The function should have a space complexity of O(1) and a time complexity of O(n).
"""

def sum_odd_no_multiples_of_3(n, current_sum=0):
    if n == 0:
        return current_sum
    elif n % 3 == 0:
        return sum_odd_no_multiples_of_3(n-1, current_sum)
    elif n % 2 == 1:
        current_sum += n
    return sum_odd_no_multiples_of_3(n-1, current_sum)