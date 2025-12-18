"""
QUESTION:
Given three arrays of integers, return the sum of elements that are common in all three arrays.

For example: 

```
common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays
```

More examples in the test cases. 

Good luck!
"""

from collections import Counter

def sum_common_elements(arr1, arr2, arr3):
    # Create Counters for each array
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    counter3 = Counter(arr3)
    
    # Find the intersection of all three Counters
    common_counter = counter1 & counter2 & counter3
    
    # Sum the elements in the common Counter
    return sum(common_counter.elements())