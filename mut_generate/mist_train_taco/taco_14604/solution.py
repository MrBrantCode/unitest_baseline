"""
QUESTION:
In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

```python
# Remove the 3's at indices 0 and 3
# followed by removing a 4 at index 1
solve([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]
```

More examples can be found in the test cases. 

Good luck!
"""

def remove_leftmost_duplicates(arr):
    result = []
    for num in arr[::-1]:
        if num not in result:
            result.append(num)
    return result[::-1]