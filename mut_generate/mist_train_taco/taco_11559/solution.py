"""
QUESTION:
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.


## Examples

```
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
```
"""

from collections import Counter

def most_frequent_largest(arr):
    # Count the frequency of each number in the array
    frequency_count = Counter(arr)
    
    # Find the maximum frequency
    max_frequency = max(frequency_count.values())
    
    # Find all numbers that have the maximum frequency
    most_frequent_numbers = [k for k, v in frequency_count.items() if v == max_frequency]
    
    # Return the largest number among the most frequent numbers
    return max(most_frequent_numbers)