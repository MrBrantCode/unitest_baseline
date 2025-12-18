"""
QUESTION:
Create a function

```python
has_two_cube_sums(n)
```

which checks if a given number `n` can be written as the sum of two cubes in two different ways: `n = a³+b³ = c³+d³`.
All the numbers `a`, `b`, `c` and `d` should be different and greater than `0`.

E.g. 1729 = 9³+10³ = 1³+12³.

```python
has_two_cube_sums(1729); // true
has_two_cube_sums(42);   // false
```
"""

def has_two_cube_sums(n):
    # Calculate the upper limit for the cube root of n
    limit = int(n ** (1.0 / 3.0)) + 1
    
    # Generate a list of cubes up to the limit
    cubic_list = [i ** 3 for i in range(1, limit)]
    
    # Dictionary to store the sums of cubes
    cube_sums = {}
    
    # Iterate through all pairs of cubes
    for i in range(len(cubic_list)):
        for j in range(i + 1, len(cubic_list)):
            sum_of_cubes = cubic_list[i] + cubic_list[j]
            if sum_of_cubes in cube_sums:
                # Check if the current pair is different from the stored pair
                if cube_sums[sum_of_cubes] != (i, j):
                    return True
            else:
                cube_sums[sum_of_cubes] = (i, j)
    
    return False