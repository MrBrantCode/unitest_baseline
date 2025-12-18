"""
QUESTION:
Create a function called `sum_and_product` that takes two parameters. The function should return the sum and product of the two parameters and format the output as "The sum of a and b is c and their product is d", replacing a, b, c, and d with the corresponding numerical values. If either parameter is not a number, the function should return an informative error message. The function should work correctly for both integer and floating point inputs.
"""

def sum_and_product(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Both inputs must be a number!"
    
    sum_ab = a + b
    product_ab = a * b

    output_message = "The sum of {} and {} is {} and their product is {}".format(a, b, sum_ab, product_ab)
    return output_message