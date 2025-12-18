"""
QUESTION:
Make a function that receives a value, ```val``` and outputs the smallest higher number than the given value, and this number belong to a set of positive integers that have the following properties:

- their digits occur only once

- they are odd

- they are multiple of three

```python
next_numb(12) == 15

next_numb(13) == 15

next_numb(99) == 105

next_numb(999999) == 1023459

next_number(9999999999) == "There is no possible number that
fulfills those requirements"
```

Enjoy the kata!!
"""

def unique_digits(n):
    return len(set(str(n))) == len(str(n))

def find_next_valid_number(val):
    val += 1
    while val % 3 != 0:
        val += 1
    if val % 2 == 0:
        val += 3
    while not unique_digits(val):
        val += 6
        if val > 9876543210:
            break
    else:
        return val
    return 'There is no possible number that fulfills those requirements'