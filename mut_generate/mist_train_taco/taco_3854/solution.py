"""
QUESTION:
A lot of goods have an  International Article Number (formerly known as "European Article Number") abbreviated "EAN". EAN is a 13-digits barcode consisting of 12-digits data followed by a single-digit checksum (EAN-8 is not considered in this kata).


The single-digit checksum is calculated as followed (based upon the 12-digit data):

The digit at the first, third, fifth, etc. position (i.e. at the odd position) has to be multiplied with "1". 
The digit at the second, fourth, sixth, etc. position (i.e. at the even position) has to be multiplied with "3".
Sum these results. 

If this sum is dividable by 10, the checksum is 0. Otherwise the checksum has the following formula:

  checksum = 10 - (sum mod 10)

For example, calculate the checksum for "400330101839" (= 12-digits data):

4·1 + 0·3 + 0·1 + 3·3 + 3·1 + 0·3 + 1·1 + 0·3 + 1·1 + 8·3 + 3·1 + 9·3
= 4 + 0 + 0 + 9 + 3 + 0 + 1 + 0 + 1 + 24 + 3 + 27 
= 72
10 - (72 mod 10) = 8 ⇒ Checksum: 8

Thus, the EAN-Code is 4003301018398 (= 12-digits data followed by single-digit checksum).
 
Your Task
Validate a given EAN-Code. Return true if the given EAN-Code is valid, otherwise false.

Assumption
You can assume the given code is syntactically valid, i.e. it only consists of numbers and it exactly has a length of 13 characters.

Examples

```python
validate_ean("4003301018398") # => True
validate_ean("4003301018392") # => False
```

Good Luck and have fun.
"""

def validate_ean(code: str) -> bool:
    """
    Validates an EAN-13 code by checking if the checksum digit is correct.

    Parameters:
    code (str): A string representing the EAN-13 code to be validated.

    Returns:
    bool: True if the EAN-13 code is valid, otherwise False.
    """
    # Extract the 12-digit data part and the checksum digit
    data_part = code[:-1]
    checksum_digit = int(code[-1])
    
    # Calculate the sum of the digits at odd positions (multiplied by 1)
    odd_sum = sum(int(data_part[i]) for i in range(0, len(data_part), 2))
    
    # Calculate the sum of the digits at even positions (multiplied by 3)
    even_sum = sum(int(data_part[i]) * 3 for i in range(1, len(data_part), 2))
    
    # Calculate the total sum
    total_sum = odd_sum + even_sum
    
    # Calculate the expected checksum
    expected_checksum = 10 - (total_sum % 10) if total_sum % 10 != 0 else 0
    
    # Validate the checksum
    return expected_checksum == checksum_digit