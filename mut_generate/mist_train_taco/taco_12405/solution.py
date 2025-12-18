"""
QUESTION:
Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there) with an array/list/vector of integers and the expected number `n` of smallest elements to return.

Also:

* the number of elements to be returned cannot be higher than the array/list/vector length;
* elements can be duplicated;
* in case of duplicates, just return them according to the original order (see third example for more clarity).

Same examples and more in the test cases:

```python
first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []
```

[Performance version by FArekkusu](https://www.codewars.com/kata/5aeed69804a92621a7000077) also available.
"""

def first_n_smallest(arr, n):
    # Step 1: Sort the array by value, but keep track of the original indices
    sorted_with_indices = sorted(enumerate(arr), key=lambda it: it[1])
    
    # Step 2: Take the first `n` elements from the sorted list
    smallest_n_with_indices = sorted_with_indices[:n]
    
    # Step 3: Sort these `n` elements back by their original indices
    smallest_n_with_indices.sort(key=lambda it: it[0])
    
    # Step 4: Extract the values from the sorted list of tuples
    result = [value for index, value in smallest_n_with_indices]
    
    return result