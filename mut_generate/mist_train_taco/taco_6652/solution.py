"""
QUESTION:
Kurt reaches nirvana when he finds the product of all the digits of some positive integer. Greater value of the product makes the nirvana deeper.

Help Kurt find the maximum possible product of digits among all integers from $1$ to $n$.


-----Input-----

The only input line contains the integer $n$ ($1 \le n \le 2\cdot10^9$).


-----Output-----

Print the maximum product of digits among all integers from $1$ to $n$.


-----Examples-----
Input
390

Output
216

Input
7

Output
7

Input
1000000000

Output
387420489



-----Note-----

In the first example the maximum product is achieved for $389$ (the product of digits is $3\cdot8\cdot9=216$).

In the second example the maximum product is achieved for $7$ (the product of digits is $7$).

In the third example the maximum product is achieved for $999999999$ (the product of digits is $9^9=387420489$).
"""

def max_digit_product(n: int) -> int:
    """
    Finds the maximum possible product of digits among all integers from 1 to n.

    Parameters:
    n (int): The upper limit for finding the maximum digit product.

    Returns:
    int: The maximum product of digits found among all integers from 1 to n.
    """
    
    def product_of_digits(num: int) -> int:
        """Helper function to calculate the product of digits of a number."""
        product = 1
        while num != 0:
            product *= num % 10
            num //= 10
        return product
    
    if n < 10:
        return n
    
    max_product = product_of_digits(n)
    past_product = 1
    
    while n != 0:
        while n % 10 != 9 and len(str(n)) != 1:
            n -= 1
        max_product = max(max_product, product_of_digits(n) * past_product)
        past_product *= n % 10
        n //= 10
    
    return max_product