"""
QUESTION:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```python
move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
```
"""

def move_zeros(arr):
    # Filter out non-zero elements and keep boolean values as they are
    non_zeros = [i for i in arr if isinstance(i, bool) or i != 0]
    
    # Calculate the number of zeros to append
    zero_count = len(arr) - len(non_zeros)
    
    # Return the combined list of non-zeros followed by zeros
    return non_zeros + [0] * zero_count