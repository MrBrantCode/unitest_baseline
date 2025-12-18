"""
QUESTION:
Identify the data types of variables in real time using metaprogramming and handle potential type errors from mathematical operations. Create a function named `sample(p, q, r)` that takes three parameters and performs various mathematical operations on them. The function should dynamically identify and print the data types of the variables after each assignment. Additionally, the function should handle potential type errors that may arise from the mathematical operations, such as subtraction, modulo, and multiplication. Ensure the function can handle a variety of data types, including numbers, strings, and complex numbers.
"""

def sample(p, q, r):
    # Ensure p, q, r are numbers
    if all(isinstance(i, (int, float)) for i in [p, q, r]):
        n = p - q - r
        print(f'The type of n is: {type(n)}')
        if q !=0 and r != 0:  # prevent ZeroDivisionError
            m = p % q % r
            print(f'The type of m is: {type(m)}')
        else:
            print("q and r should not be 0")
            return
        o = n * m
        print(f'The type of o is: {type(o)}')
    else:
        print("p, q, and r should be numbers")
        return

    x = [p, q, r, n, m, o]
    print(f'The type of x is: {type(x)}')
    y = "pqrnmo"
    print(f'The type of y is: {type(y)}')