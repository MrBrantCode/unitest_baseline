"""
QUESTION:
Design a function `classify_number(n)` that takes an integer `n` as input and returns a tuple containing the parity of `n` as a string ('Even' or 'Odd') and its classification as a string ('Prime', 'Composite', or 'Neither prime nor composite'). The function should correctly classify numbers, including the edge cases where `n` is 0 or 1.
"""

# This function checks if a number is prime by checking for divisibility on numbers less than it.
# It returns a boolean True if it is a prime number and False otherwise
def check_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for current in range(3, int(n ** 0.5) + 1, 2):
        if n % current == 0: 
            return False
    return True

def classify_number(n):
    if n % 2 == 0: 
        parity = 'Even'
    else:
        parity = 'Odd'
        
    if check_prime(n): 
        classification = 'Prime'
    elif n == 1 or n == 0: 
        classification = 'Neither prime nor composite'
    else: 
        classification = 'Composite'
    return parity, classification