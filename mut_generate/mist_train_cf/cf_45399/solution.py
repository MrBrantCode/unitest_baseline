"""
QUESTION:
Design a function named `conjugate_product` that takes two complex numbers as input and returns their conjugate product. The function must validate that both inputs are complex numbers and handle potential exceptions. The function should prioritize time efficiency, as it will be used with large datasets. The function should return an error message if the inputs are not complex numbers.
"""

def conjugate_product(c1, c2):
    if not (isinstance(c1, complex) and isinstance(c2, complex)):
        return 'Inputs have to be complex numbers'

    conj_c1 = c1.conjugate()
    conj_c2 = c2.conjugate()
    product = conj_c1 * conj_c2
    return product