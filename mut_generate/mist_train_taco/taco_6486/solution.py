"""
QUESTION:
## Snail Sort

Given an `n x n` array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

```
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
```

For better understanding, please follow the numbers of the next array consecutively:

```
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
```

This image will illustrate things more clearly:



NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array `[[]]`.
"""

def snail_sort(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in range((size + 1) // 2):
            for x in range(n, size - n):
                ret.append(array[n][x])
            for y in range(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in range(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in range(2 + n, size - n):
                ret.append(array[-y][n])
    return ret