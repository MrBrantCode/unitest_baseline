"""
QUESTION:
Create a function named `multiply_in_second_iteration` that modifies a while loop so that the variable `product` is multiplied by `j` every second iteration. The function should take two parameters, `j` and `n`, where `j` is the number by which `product` will be multiplied, and `n` is the number of iterations the loop will run. The initial value of `product` should be 1.
"""

def multiply_in_second_iteration(j, n):
    """
    Modifies a while loop so that the variable product is multiplied by j every second iteration.

    Args:
        j (int): The number by which product will be multiplied.
        n (int): The number of iterations the loop will run.

    Returns:
        int: The final product after n iterations.
    """

    product = 1 
    i = 0
    
    while i < n: 
        i += 1

        if i % 2 == 0: 
            product = product * j

    return product