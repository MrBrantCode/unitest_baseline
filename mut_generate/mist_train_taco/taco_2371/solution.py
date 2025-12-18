"""
QUESTION:
Given a list of integers, return the nth smallest integer in the list. **Only distinct elements should be considered** when calculating the answer. `n` will always be positive (`n > 0`)

If the nth small integer doesn't exist, return `-1` (C++) / `None` (Python) / `nil` (Ruby) / `null` (JavaScript).

Notes:
* "indexing" starts from 1
* huge lists (of 1 million elements) will be tested

## Examples

```python
nth_smallest([1, 3, 4, 5], 7)        ==> None  # n is more than the size of the list
nth_smallest([4, 3, 4, 5], 4)        ==> None  # 4th smallest integer doesn't exist
nth_smallest([45, -10, 4, 5, 4], 4)  ==> 45    # 4th smallest integer is 45
```

If you get a timeout, just try to resubmit your solution. However, if you ***always*** get a timeout, review your code.
"""

def find_nth_smallest(arr, n):
    # Convert the list to a set to remove duplicates
    unique_elements = set(arr)
    
    # Check if the requested nth smallest element exists
    if n > len(unique_elements):
        return None
    
    # Sort the unique elements and return the nth smallest
    sorted_elements = sorted(unique_elements)
    return sorted_elements[n - 1]