"""
QUESTION:
# Task
 John loves encryption. He can encrypt any string by the following algorithm:
```
take the first and the last letters of the word;
replace the letters between them with their number;
replace this number with the sum of it digits 
          until a single digit is obtained.```
Given two strings(`s1` and `s2`), return `true` if their encryption is the same, or `false` otherwise.

# Example

 For `s1 = "EbnhGfjklmjhgz" and s2 = "Eabcz"`, the result should be `true`.
 ```
 "EbnhGfjklmjhgz" --> "E12z" --> "E3z"
 "Eabcz" --> "E3z"
 Their encryption is the same.```
 
# Input/Output


 - `[input]` string `s1`

  The first string to be encrypted.
  
  `s1.length >= 3`
 
 
 - `[input]` string `s2`

  The second string to be encrypted.

  `s2.length >= 3`
  
  
 - `[output]` a boolean value

 `true` if encryption is the same, `false` otherwise.
"""

def are_encryptions_same(s1: str, s2: str) -> bool:
    """
    Determines if the encryptions of two given strings are the same.

    The encryption algorithm is as follows:
    1. Take the first and the last letters of the word.
    2. Replace the letters between them with their number.
    3. Replace this number with the sum of its digits until a single digit is obtained.

    Parameters:
    - s1 (str): The first string to be encrypted.
    - s2 (str): The second string to be encrypted.

    Returns:
    - bool: True if the encryptions are the same, False otherwise.
    """
    def single_digit_sum(n: int) -> int:
        """Helper function to reduce a number to a single digit by summing its digits."""
        while n >= 10:
            n = sum(int(digit) for digit in str(n))
        return n

    # Calculate the single digit sum of the length of the string
    len_s1_single_digit = single_digit_sum(len(s1) - 2)
    len_s2_single_digit = single_digit_sum(len(s2) - 2)

    # Compare the first and last characters and the single digit sum of the lengths
    return (s1[0], s1[-1], len_s1_single_digit) == (s2[0], s2[-1], len_s2_single_digit)