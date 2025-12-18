"""
QUESTION:
Write a function `custom_sort` that takes a list of positive integers as input and returns the sorted list in ascending order. The sorting should be based on two keys: 
- The primary key is the sum of the digits of each integer.
- If the sums are equal, the secondary key is the last digit of each integer.
"""

def custom_sort(arr):
    def get_digit_sum(num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum
    
    arr.sort(key=lambda x: (get_digit_sum(x), x % 10))
    return arr