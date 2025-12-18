"""
QUESTION:
Create a function `base10_to_base8(n)` that converts a base 10 number `n` to base 8, handling both negative numbers and floating-point numbers with 4 decimal precision. The function should return a string representing the base 8 equivalent of `n`.
"""

def base10_to_base8(n):
    if n < 0:
        return "-" + base10_to_base8(-n)
    if "." in str(n):
        whole, fraction = str(n).split(".")
        whole = oct(int(whole))[2:]
        fraction = float("0." + fraction)
        fraction_oct = ""
        while len(fraction_oct) < 4:
            fraction *= 8
            digit, fraction = divmod(fraction, 1)
            fraction_oct += str(int(digit))
        return "{}.{}".format(whole, fraction_oct)
    else:
        return oct(int(n))[2:]