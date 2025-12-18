"""
QUESTION:
You get an array of different numbers to sum up. But there is one problem, those numbers all have different bases.
For example:
```python
You get an array of numbers with their base as an input:

[["101",16],["7640",8],["1",9]]
```

The output should be the sum as an integer value with a base of 10, so according to the example this would be:

4258
```python
A few more examples:
[["101",2], ["10",8]] --> 13
[["ABC",16], ["11",2]] --> 2751
```
Bases can be between 2 and 36 (2<=base<=36)
"""

def sum_numbers_with_bases(numbers_with_bases):
    """
    Sums numbers given in different bases and returns the result in base 10.

    Parameters:
    numbers_with_bases (list of lists): A list where each element is a list containing a string representation of a number and its base.

    Returns:
    int: The sum of all the numbers converted to base 10.
    """
    return sum(int(number, base) for number, base in numbers_with_bases)