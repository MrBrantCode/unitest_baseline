"""
QUESTION:
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

```python
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
```

Return -1 (for `Haskell`: return `Nothing`, for `Rust`: return `None`), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

```python 
next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
```
```ruby 
next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
```

 * some tests will include very large numbers.
 * test data only employs positive integers.

*The function you write for this challenge is the inverse of this kata: "[Next bigger number with the same digits](http://www.codewars.com/kata/next-bigger-number-with-the-same-digits)."*
"""

def next_smaller_with_same_digits(n):
    s = list(str(n))
    i = j = len(s) - 1
    
    # Find the first digit that is larger than the digit next to it
    while i > 0 and s[i - 1] <= s[i]:
        i -= 1
    
    # If no such digit is found, return -1
    if i <= 0:
        return -1
    
    # Find the largest digit on the right side of (i-1)th digit that is smaller than s[i-1]
    while s[j] >= s[i - 1]:
        j -= 1
    
    # Swap the found digit with the (i-1)th digit
    (s[i - 1], s[j]) = (s[j], s[i - 1])
    
    # Reverse the digits after (i-1)th digit to get the smallest permutation
    s[i:] = reversed(s[i:])
    
    # If the result has a leading zero, return -1
    if s[0] == '0':
        return -1
    
    # Convert the list back to an integer and return
    return int(''.join(s))