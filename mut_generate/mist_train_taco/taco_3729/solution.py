"""
QUESTION:
Create a function named `divisors`/`Divisors` that takes an integer `n > 1` and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (`null` in C#) (use `Either String a` in Haskell and `Result, String>` in Rust).

#### Example:

```python
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
```
"""

def divisors(n):
    # List comprehension to find all divisors of n (excluding 1 and n)
    divisors_list = [i for i in range(2, n) if n % i == 0]
    
    # Check if the list is empty (i.e., n is prime)
    if not divisors_list:
        return f"{n} is prime"
    
    # Return the list of divisors
    return divisors_list