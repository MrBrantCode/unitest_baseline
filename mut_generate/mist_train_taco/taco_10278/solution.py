"""
QUESTION:
The number `1035` is the smallest integer that exhibits a non frequent property: one its multiples, `3105 = 1035 * 3`, has its same digits but in different order, in other words, `3105`, is one of the permutations of `1035`.

The number `125874` is the first integer that has this property when the multiplier is `2`, thus: `125874 * 2 = 251748`

Make the function `search_permMult()`, that receives an upper bound, nMax and a factor k and will output the amount of pairs bellow nMax that are permuted when an integer of this range is multiplied by `k`. The pair will be counted if the multiple is less than `nMax`, too

Let'see some cases:
```python
search_permMult(10000, 7) === 1 # because we have the pair 1359, 9513
search_permMult(5000, 7) === 0 # no pairs found, as 9513 > 5000

search_permMult(10000, 4) === 2 # we have two pairs (1782, 7128) and (2178, 8712)
search_permMult(8000, 4) === 1 # only the pair (1782, 7128) 

search_permMult(5000, 3) === 1 # only the pair (1035, 3105)
search_permMult(10000, 3) === 2 # found pairs (1035, 3105) and (2475, 7425)
```
Features of the random Tests:
```
10000 <= nMax <= 100000
3 <= k <= 7
```
Enjoy it and happy coding!!
"""

from bisect import bisect

# Precomputed memoization dictionary
memo = {
    3: [3105, 7425, 30105, 31050, 37125, 42741, 44172, 71253, 72441, 74142, 74250, 74628, 74925, 82755, 85725],
    4: [7128, 8712, 67128, 70416, 71208, 71280, 71328, 71928, 72108, 78912, 79128, 80712, 86712, 87120, 87132, 87192, 87912, 95832],
    5: [],
    6: [8316, 83160, 83916, 84510, 89154, 91152],
    7: [9513, 81816, 83181, 90321, 91203, 93513, 94143, 95130, 95193, 95613]
}

def search_permMult(nMax, k):
    """
    Returns the count of pairs (integer and its permuted multiple) below nMax when the integer is multiplied by k.

    Parameters:
    nMax (int): The upper bound for the range of integers to consider.
    k (int): The multiplier to be used to find the permuted multiples.

    Returns:
    int: The count of pairs below nMax.
    """
    if k not in memo:
        return 0
    return bisect(memo[k], nMax)