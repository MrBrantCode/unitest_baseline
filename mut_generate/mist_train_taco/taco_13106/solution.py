"""
QUESTION:
Given a string, turn each letter into its ASCII character code and join them together to create a number - let's call this number `total1`:

```
'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
```

Then replace any incidence of the number `7` with the number `1`, and call this number 'total2':
```
total1 = 656667
              ^
total2 = 656661
              ^
```

Then return the difference between the sum of the digits in `total1` and `total2`:

```
  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6
```
"""

def calculate_ascii_difference(input_string: str) -> int:
    # Step 1: Convert each character to its ASCII code and join them to form total1
    total1 = ''.join(str(ord(c)) for c in input_string)
    
    # Step 2: Replace '7' with '1' to form total2
    total2 = total1.replace('7', '1')
    
    # Step 3: Calculate the sum of digits in total1 and total2
    sum_total1 = sum(int(digit) for digit in total1)
    sum_total2 = sum(int(digit) for digit in total2)
    
    # Step 4: Return the difference between the sums
    return sum_total1 - sum_total2