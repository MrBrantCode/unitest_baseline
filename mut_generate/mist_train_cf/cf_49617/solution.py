"""
QUESTION:
Create a function `separate_arrays` that takes a list of prime numbers less than 10000 and returns two lists. The first list should contain prime numbers where the sum of their digits is even, and the second list should contain prime numbers where the sum of their digits is odd.
"""

def separate_arrays(arr):
    even_sums = []
    odd_sums = []

    for num in arr:
        # Calculate the sum of digits
        digits_sum = sum(int(digit) for digit in str(num))
        
        # Check if the sum is even or odd
        if digits_sum % 2 == 0:
            even_sums.append(num)
        else:
            odd_sums.append(num)

    return even_sums, odd_sums