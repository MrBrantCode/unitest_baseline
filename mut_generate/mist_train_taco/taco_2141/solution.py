"""
QUESTION:
We have an array of unique elements. A special kind of permutation is the one that has all of its elements in a different position than the original.

Let's see how many of these permutations may be generated from an array of four elements. We put the original array with square brackets and the wanted permutations with parentheses. 
```
arr = [1, 2, 3, 4]
      (2, 1, 4, 3)
      (2, 3, 4, 1)
      (2, 4, 1, 3)
      (3, 1, 4, 2)
      (3, 4, 1, 2)
      (3, 4, 2, 1)
      (4, 1, 2, 3)
      (4, 3, 1, 2)
      (4, 3, 2, 1)
      _____________
A total of 9 permutations with all their elements in different positions than arr
```

The task for this kata would be to create a code to count all these permutations for an array of certain length.

Features of the random tests:
```
l = length of the array
10 ≤ l ≤ 5000
```

See the example tests.

Enjoy it!
"""

def count_derangements(n: int) -> int:
    """
    Counts the number of derangements (permutations where no element appears in its original position)
    for an array of length `n`.

    Parameters:
    n (int): The length of the array.

    Returns:
    int: The number of derangements.
    """
    if n == 0:
        return 1  # By definition, the number of derangements of an empty array is 1.
    if n == 1:
        return 0  # There is no way to derange a single element array.
    
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, (i + 1) * (a + b)
    return a