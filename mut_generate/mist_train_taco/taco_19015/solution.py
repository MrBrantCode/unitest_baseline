"""
QUESTION:
Your task it to return ```true``` if the fractional part (rounded to 1 digit) of the result (```a``` / ```b```) exists, more than ```0``` and is multiple of ```n```.
Otherwise return ```false```. (For Python return True or False)

All arguments are positive digital numbers.

Rounding works like toFixed() method. (if more than...5 rounds up)

Find exapmles below: 

```

isMultiple(5, 2, 3) -> false // 2.5 -> 5 is not multiple of 3
isMultiple(5, 3, 4) -> false // 1.7 -> 7 is not multiple of 4
isMultiple(5, 4, 3) -> true // 1.3 -> 3 is multiple of 3
isMultiple(666, 665, 2) -> false // 1.0 -> return false


```
"""

def is_fractional_part_multiple(a: int, b: int, n: int) -> bool:
    # Calculate the fractional part rounded to 1 digit
    remainder = int((a / b + 0.05) * 10) % 10
    
    # Check if the remainder is more than 0 and a multiple of n
    return remainder > 0 and remainder % n == 0