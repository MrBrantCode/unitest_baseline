"""
QUESTION:
Make the 2D list by the sequential integers started by the ```head``` number.

See the example test cases for the expected output.

``` 
Note:

-10**20 < the head number <10**20
1 <=  the number of rows <= 1000
0 <=  the number of columms <= 1000
```
"""

def generate_2d_list(head, rows, cols):
    """
    Generates a 2D list filled with sequential integers starting from the given head number.

    Parameters:
    head (int): The starting integer for the sequence.
    rows (int): The number of rows in the 2D list.
    cols (int): The number of columns in the 2D list.

    Returns:
    list: A 2D list (list of lists) where each element is a sequential integer starting from `head`.
    """
    return [[head + c + r * cols for c in range(cols)] for r in range(rows)]