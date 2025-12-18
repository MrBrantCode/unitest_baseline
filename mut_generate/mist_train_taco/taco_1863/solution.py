"""
QUESTION:
A Madhav array has the following property:

```a[0] = a[1] + a[2] = a[3] + a[4] + a[5] = a[6] + a[7] + a[8] + a[9] = ...```

Complete the function/method that returns `true` if the given array is a Madhav array, otherwise it returns `false`.

*Edge cases: An array of length* `0` *or* `1` *should not be considered a Madhav array as there is nothing to compare.*
"""

def is_madhav_array(arr):
    # Edge case: An array of length 0 or 1 should not be considered a Madhav array
    if len(arr) <= 1:
        return False
    
    # Calculate the number of terms in the Madhav array sequence
    nTerms = ((1 + 8 * len(arr)) ** 0.5 - 1) / 2
    
    # Check if nTerms is an integer
    if nTerms % 1 != 0:
        return False
    
    nTerms = int(nTerms)
    
    # Check the Madhav array property
    expected_sum = arr[0]
    for i in range(1, nTerms + 1):
        start_index = i * (i - 1) // 2
        end_index = start_index + i
        if sum(arr[start_index:end_index]) != expected_sum:
            return False
    
    return True