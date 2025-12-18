"""
QUESTION:
Complete the function/method (depending on the language) to return `true`/`True` when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

```python
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
```

~~~if:javascript
For your convenience, there is already a function 'isArray(o)' declared and defined that returns true if its argument is an array, false otherwise.
~~~

~~~if:php
You may assume that all arrays passed in will be non-associative.
~~~
"""

def same_structure_as(original, other):
    # Check if both inputs are lists and have the same length
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        # Iterate through corresponding elements in both lists
        for o1, o2 in zip(original, other):
            # Recursively check the structure of nested elements
            if not same_structure_as(o1, o2):
                return False
        # If all elements have the same structure, return True
        return True
    else:
        # If one of the inputs is not a list, check if both are not lists
        return not isinstance(original, list) and not isinstance(other, list)