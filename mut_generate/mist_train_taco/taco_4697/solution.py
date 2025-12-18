"""
QUESTION:
##Task:
You have to write a function `add` which takes two binary numbers as strings and returns their sum as a string.

##Note:
* You are `not allowed to convert binary to decimal & vice versa`.
* The sum should contain `No leading zeroes`.

##Examples:
```
add('111','10'); => '1001'
add('1101','101'); => '10010'
add('1101','10111') => '100100'
```
"""

def add_binary_strings(a: str, b: str) -> str:
    # Initialize pointers for both strings
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    
    # Loop until both strings are processed
    while i >= 0 or j >= 0 or carry:
        # Get the current digits from both strings, or 0 if the string is exhausted
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        # Calculate the sum of the current digits and the carry
        total = digit_a + digit_b + carry
        
        # Append the least significant bit of the total to the result
        result.append(str(total % 2))
        
        # Update the carry
        carry = total // 2
        
        # Move to the next digits
        i -= 1
        j -= 1
    
    # The result is in reverse order, so reverse it before returning
    return ''.join(result[::-1])