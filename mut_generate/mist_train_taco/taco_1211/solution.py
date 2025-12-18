"""
QUESTION:
You have an array of numbers.  
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

*Example*
```python
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
```
"""

def sort_array_preserve_even(arr):
    # Extract and sort odd numbers in ascending order
    odds = sorted((x for x in arr if x % 2 != 0))
    
    # Create a new list where odd numbers are replaced by sorted odds
    result = [odds.pop(0) if x % 2 != 0 else x for x in arr]
    
    return result