"""
QUESTION:
# Task:
Given a list of numbers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching `"odd"` or `"even"`.

If the input array is empty consider it as: `[0]` (array with a zero).

## Example:

```
odd_or_even([0])          ==  "even"
odd_or_even([0, 1, 4])    ==  "odd"
odd_or_even([0, -1, -5])  ==  "even"
```

Have fun!
"""

def determine_sum_parity(arr):
    # If the input array is empty, consider it as [0]
    if not arr:
        arr = [0]
    
    # Calculate the sum of the elements in the array
    total_sum = sum(arr)
    
    # Determine if the sum is odd or even
    if total_sum % 2 == 0:
        return "even"
    else:
        return "odd"