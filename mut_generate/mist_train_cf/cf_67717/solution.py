"""
QUESTION:
Create a function called `sort_complex_numbers` that categorizes a list of complex numbers into a dictionary based on whether their imaginary parts are prime numbers or not. The dictionary should have two keys: "Prime" and "Not Prime". The function should take a list of complex numbers as input and return a dictionary where the values are lists of complex numbers corresponding to the keys. 

The function should work with any list of complex numbers, not just the provided example.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def sort_complex_numbers(complex_set):
    complex_dict = {"Prime": [], "Not Prime": []}
    for complex_num in complex_set:
        if is_prime(complex_num.imag):
            complex_dict["Prime"].append(complex_num)
        else:
            complex_dict["Not Prime"].append(complex_num)
    return complex_dict