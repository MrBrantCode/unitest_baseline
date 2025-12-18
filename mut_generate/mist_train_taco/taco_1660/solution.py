"""
QUESTION:
The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

The result array should be sorted in ascending order of values.

Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.


## Examples
~~~if-not:python
```
[1, 2, 3, 4]  should return [[1, 3], [2, 4]]

[4, 1, 2, 3]  should also return [[1, 3], [2, 4]]

[1, 23, 3, 4, 7] should return [[1, 3]]

[4, 3, 1, 5, 6] should return [[1, 3], [3, 5], [4, 6]]
```
~~~
~~~if:python
```
[1, 2, 3, 4]  should return [(1, 3), (2, 4)]

[4, 1, 2, 3]  should also return [(1, 3), (2, 4)]

[1, 23, 3, 4, 7] should return [(1, 3)]

[4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]
```
~~~
"""

def find_pairs_with_difference(arr):
    # Convert the array to a set for O(1) lookups
    s = set(arr)
    
    # Generate pairs where the difference is 2
    pairs = [(x, x + 2) for x in arr if x + 2 in s]
    
    # Sort the pairs in ascending order
    return sorted(pairs)