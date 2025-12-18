"""
QUESTION:
Create a function `sort_complex_numbers` that sorts a list of complex numbers based on two conditions: 
1. The frequency of their real part occurring in the list (in descending order).
2. The magnitude of their imaginary parts for those with equal frequencies (in descending order).

Input: A list of complex numbers.
Output: A sorted list of complex numbers according to the specified conditions.
"""

def sort_complex_numbers(numbers):
    # create a dictionary to count the frequency of the real parts
    real_freq = {}
    for num in numbers:
        if num.real in real_freq:
            real_freq[num.real] += 1
        else:
            real_freq[num.real] = 1

    # sort the list based on the given conditions
    numbers.sort(key=lambda num: (-real_freq[num.real], -abs(num.imag)))
    
    return numbers