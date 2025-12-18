"""
QUESTION:
Given an array with exactly 5 strings `"a"`, `"b"` or `"c"` (`char`s in Java, `character`s in Fortran), check if the array contains three and two of the same values.

## Examples

```
["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a"
```
"""

def check_three_and_two(array):
    # Ensure the array has exactly 5 elements
    if len(array) != 5:
        raise ValueError("The array must contain exactly 5 elements.")
    
    # Count the occurrences of each unique element in the array
    counts = {array.count(x) for x in set(array)}
    
    # Check if the counts match the required pattern {2, 3}
    return counts == {2, 3}