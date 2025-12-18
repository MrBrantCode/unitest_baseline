"""
QUESTION:
Given an array containing only zeros and ones, find the index of the zero that, if converted to one, will make the longest sequence of ones.

For instance, given the array:

```
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
```

replacing the zero at index 10 (counting from 0) forms a sequence of 9 ones:

```
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1]
                  '------------^------------'
```


Your task is to complete the function that determines where to replace a zero with a one to make the maximum length subsequence.


**Notes:**
- If there are multiple results, return the last one:

 `[1, 1, 0, 1, 1, 0, 1, 1] ==> 5`


- The array will always contain only zeros and ones.


Can you do this in one pass?
"""

def find_best_zero_to_replace(arr):
    max_length = 0
    best_index = -1
    current_length = 0
    previous_length = 0
    zero_index = -1
    
    for i in range(len(arr)):
        if arr[i] == 1:
            current_length += 1
        else:
            if i > 0 and arr[i-1] == 1:
                candidate_length = previous_length + 1 + current_length
                if candidate_length >= max_length:
                    max_length = candidate_length
                    best_index = zero_index
            previous_length = current_length
            current_length = 0
            zero_index = i
    
    # Check the last segment
    if arr[-1] == 1:
        candidate_length = previous_length + 1 + current_length
        if candidate_length >= max_length:
            max_length = candidate_length
            best_index = zero_index
    
    return best_index