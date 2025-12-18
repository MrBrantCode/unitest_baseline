"""
QUESTION:
Write a function `multiply_abs_values_v3` that takes a list of floating-point numbers as input and returns the product of the absolute values based on their nearest rounded-down integers. Consider negative float values with decimal part 0.5 and above as positive. Eliminate elements that are divisible by any prime number less than 10, and treat negative zero as a distinct value.
"""

def multiply_abs_values_v3(lst):
    product = 1
    primes = [2, 3, 5, 7]

    for idx, val in enumerate(lst):
        if val == 0 and str(lst[idx])[0] == "-":
            product *= -1
        elif val < 0 and (abs(val) - abs(int(val))) >= 0.5:
            product *= int(abs(val))
        else:
            val = int(abs(val))
            for p in primes:
                if val % p == 0:
                    break
            else:  
                product *= val 

    return product