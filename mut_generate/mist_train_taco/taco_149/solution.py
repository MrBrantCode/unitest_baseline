"""
QUESTION:
## Task

Write a function that accepts two arguments and generates a sequence containing the integers from the first argument to the second inclusive. 

## Input

Pair of integers greater than or equal to `0`. The second argument will always be greater than or equal to the first. 

## Example

```python
generate_integers(2, 5) # --> [2, 3, 4, 5]
```
"""

def generate_sequence(start: int, end: int) -> list[int]:
    return list(range(start, end + 1))