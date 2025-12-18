"""
QUESTION:
Write a function named `lcm_prime_numbers` that takes a list of non-sequential prime numbers as input and returns their least common multiple. The function assumes the input list contains only prime numbers and does not verify this.
"""

def lcm_prime_numbers(num_list):
    # Initialize LCM to 1
    lcm = 1

    # Multiply all the numbers in the list
    # Since the numbers are prime, the LCM is their product
    for num in num_list:
        lcm *= num

    return lcm