"""
QUESTION:
# Task
 You are given three integers `l, d and x`. Your task is:
```
• determine the minimal integer n 
    such that l ≤ n ≤ d, and the sum of its digits equals x.
• determine the maximal integer m 
    such that l ≤ m ≤ d, and the sum of its digits equals x.
```
It is guaranteed that such numbers always exist.

# Input/Output


 - `[input]` integer `l`

 - `[input]` integer `d`

  `1 ≤ l ≤ d ≤ 10000.`


 - `[input]` integer `x`

  `1 ≤ x ≤ 36`


 - `[output]` an integer array

  Array of two elements, where the first element is `n`, and the second one is `m`.


# Example

 For `l = 500, d = 505, x = 10`, the output should be `[505, 505]`.
 
 For `l = 100, d = 200, x = 10`, the output should be `[109, 190]`.
"""

def find_min_max_with_digit_sum(l, d, x):
    def digit_sum(num):
        return sum(map(int, str(num)))
    
    valid_numbers = [num for num in range(l, d + 1) if digit_sum(num) == x]
    return [min(valid_numbers), max(valid_numbers)]