"""
QUESTION:
Create a function `multiplication_table` to generate the multiplication table of a given number `n`, but only for odd numbers, up to a specified limit `limit`. The function should use list comprehension and return the table as a string with each row separated by a newline.
"""

def multiplication_table(n, limit):
    """
    Generate the multiplication table of a given number `n`, but only for odd numbers, up to a specified limit `limit`.
    
    Args:
        n (int): The number for which the multiplication table is generated.
        limit (int): The upper limit of the multiplication table.
    
    Returns:
        str: The multiplication table as a string with each row separated by a newline.
    """
    return "\n".join([f"{n} x {i} = {n*i}" for i in range(1, limit + 1) if i % 2 != 0])