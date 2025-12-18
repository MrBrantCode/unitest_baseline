"""
QUESTION:
# Task
 You are given a decimal number `n` as a **string**. Transform it into an array of numbers (given as **strings** again), such that each number has only one nonzero digit and their sum equals n.

 Each number in the output array should be written without any leading and trailing zeros.

# Input/Output


 - `[input]` string `n`

 A non-negative number.
 
 `1 ≤ n.length ≤ 30.`


 - `[output]` a string array

  Elements in the array should be sorted in descending order.


# Example

 For `n = "7970521.5544"` the output should be:
 ```
 ["7000000", 
 "900000", 
 "70000", 
 "500", 
 "20", 
 "1", 
 ".5",
 ".05",
 ".004",
 ".0004"]
  ```
 For `n = "7496314"`, the output should be:
 ```
 ["7000000", 
 "400000", 
 "90000", 
 "6000", 
 "300", 
 "10", 
 "4"]
```

 For `n = "0"`, the output should be `[]`
"""

def split_decimal_to_array(n: str) -> list[str]:
    dot_index = n.find('.')
    if dot_index == -1:
        dot_index = len(n)
    
    result = []
    for i, d in enumerate(n):
        if i != dot_index and d != '0':
            if i < dot_index:
                result.append(d + '0' * (dot_index - i - 1))
            else:
                result.append(f".{'0' * (i - dot_index - 1)}{d}")
    
    return result