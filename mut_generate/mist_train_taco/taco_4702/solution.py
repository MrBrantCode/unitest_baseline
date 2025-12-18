"""
QUESTION:
Implement a function which takes a string, and returns its hash value.

Algorithm steps:

* `a` := sum of the ascii values of the input characters
* `b` := sum of every difference between the consecutive characters of the input (second char minus first char, third minus second, ...)
* `c` := (`a` OR `b`) AND ((NOT `a`) shift left by 2 bits)
* `d` := `c` XOR (32 * (`total_number_of_spaces` + 1))
* return `d`

**Note**: OR, AND, NOT, XOR are bitwise operations.

___

### Examples

```
input = "a"
a = 97
b = 0
result = 64

input = "ca"
a = 196
b = -2
result = -820
```

___

Give an example why this hashing algorithm is bad?
"""

def calculate_hash(s: str) -> int:
    # Step 1: Calculate 'a'
    a = sum(ord(c) for c in s)
    
    # Step 2: Calculate 'b'
    b = sum(ord(b) - ord(a) for a, b in zip(s, s[1:]))
    
    # Step 3: Calculate 'c'
    c = (a | b) & (~a << 2)
    
    # Step 4: Calculate 'd'
    d = c ^ (32 * (s.count(' ') + 1))
    
    # Step 5: Return 'd'
    return d