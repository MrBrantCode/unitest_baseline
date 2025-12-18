"""
QUESTION:
You have to rebuild a string from an enumerated list.
For this task, you have to check if input is correct beforehand.

* Input must be a list of tuples
* Each tuple has two elements.
* Second element is an alphanumeric character.
* First element is the index of this character into the reconstructed string.
* Indexes start at 0 and have to match with output indexing: no gap is allowed.
* Finally tuples aren't necessarily ordered by index.

If any condition is invalid, the function should return `False`.

Input example: 
```python 
[(4,'y'),(1,'o'),(3,'t'),(0,'m'),(2,'n')]
```
Returns

```python
'monty'
```
"""

def reconstruct_string(enum_list):
    try:
        # Convert the list of tuples to a dictionary for quick lookup
        nums = dict(enum_list)
        
        # Find the maximum index to determine the length of the reconstructed string
        maximum = max(nums) + 1
        
        # Reconstruct the string by joining characters based on their indices
        result = ''.join((nums[a] for a in range(maximum)))
        
        # Check if the result is alphanumeric and has the correct length
        if result.isalnum() and len(result) == maximum:
            return result
    except (KeyError, TypeError, ValueError):
        # Catch any exceptions that might occur due to invalid input
        pass
    
    # Return False if any condition is not met
    return False