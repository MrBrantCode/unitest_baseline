"""
QUESTION:
Write a function `compute_e` to calculate the value of Euler's number ("e") to the 6th decimal place. The function should take an optional integer parameter `max_iter` representing the maximum number of iterations for the series expansion of "e". The function should properly handle precision-related issues and return the most accurate possible result.
"""

def compute_e(max_iter=100):
    e_val = 2.0  
    fact = 2    

    for i in range(2, max_iter+1):
        e_val += 1.0 / fact 
        fact *= i+1 

    e_val = round(e_val, 6)

    return e_val