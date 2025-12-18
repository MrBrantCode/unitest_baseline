"""
QUESTION:
Return the `n`th term of the Recamán's sequence.

```
a(0) = 0;

        a(n-1) - n, if this value is positive and not yet in the sequence
      /
a(n) <
      \
        a(n-1) + n, otherwise
```

___

A video about Recamán's sequence by Numberphile: https://www.youtube.com/watch?v=FGC5TdIiT9U
"""

def get_recaman_term(n: int) -> int:
    """
    Returns the nth term of the Recamán's sequence.

    Parameters:
    n (int): The term index in the Recamán's sequence.

    Returns:
    int: The nth term of the Recamán's sequence.
    """
    if n < 0:
        raise ValueError("The term index n must be a non-negative integer.")
    
    series = {0}
    last = 0
    
    for i in range(1, n + 1):
        test = last - i
        if test < 0 or test in series:
            last += i
        else:
            last = test
        series.add(last)
    
    return last