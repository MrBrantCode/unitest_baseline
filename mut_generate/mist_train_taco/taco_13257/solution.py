"""
QUESTION:
Given a certain integer ```n```, we need a function ```big_primefac_div()```, that give an array with the highest prime factor and the highest divisor (not equal to n).

Let's see some cases:
```python
big_primefac_div(100) == [5, 50]
big_primefac_div(1969) == [179, 179]
```
If n is a prime number the function will output an empty list:
```python
big_primefac_div(997) == []
```
If ```n``` is an negative integer number, it should be considered the division with tha absolute number of the value.
```python
big_primefac_div(-1800) == [5, 900]
```
If ```n``` is a float type, will be rejected if it has a decimal part with some digits different than 0. The output "The number has a decimal part. No Results". But  ```n ``` will be converted automatically to an integer if all the digits of the decimal part are 0.

```python
big_primefac_div(-1800.00) == [5, 900]
big_primefac_div(-1800.1) == "The number has a decimal part. No Results"
```
Optimization and fast algorithms are a key factor to solve this kata.
Happy coding and enjoy it!
"""

def find_highest_prime_factor_and_divisor(n):
    # Check if n has a non-zero decimal part
    if isinstance(n, float) and n % 1 != 0:
        return "The number has a decimal part. No Results"
    
    # Convert n to an integer if it's a float with a zero decimal part
    n = abs(int(n))
    
    # Initialize variables
    highest_prime_factor = 0
    highest_divisor = 1
    factors = []
    
    # Copy of n for finding the highest divisor
    n_copy = n
    
    # Find prime factors
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    
    # If n is still greater than 1, it is a prime factor
    if n > 1:
        factors.append(n)
    
    # Find the highest prime factor
    if factors:
        highest_prime_factor = max(factors)
    
    # Find the highest divisor (not equal to n)
    if factors:
        highest_divisor = n_copy // factors[0]
    
    # If no prime factors or the highest divisor is 1, return an empty list
    if highest_prime_factor == 0 or highest_divisor == 1:
        return []
    
    # Return the result as a list
    return [highest_prime_factor, highest_divisor]