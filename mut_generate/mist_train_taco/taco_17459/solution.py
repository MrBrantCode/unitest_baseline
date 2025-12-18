"""
QUESTION:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are: 

* 232
* 110011
* 54322345

Complete the function to test if the given number (`num`) **can be rearranged** to form a numerical palindrome or not. Return a boolean (`true` if it can be rearranged to a palindrome, and `false` if it cannot). Return `"Not valid"` if the input is not an integer or is less than 0.

For this kata, single digit numbers are **NOT** considered numerical palindromes.  


## Examples

```
5        =>  false
2121     =>  true
1331     =>  true 
3357665  =>  true 
1294     =>  false 
"109982" =>  "Not valid"
-42      =>  "Not valid"
```
"""

from collections import Counter

def can_form_palindrome(num):
    # Check if the input is a valid integer and non-negative
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    
    # Single digit numbers are not considered palindromes
    if num < 10:
        return False
    
    # Count the frequency of each digit
    digit_counts = Counter(str(num))
    
    # Count the number of digits with odd frequencies
    odd_count = sum(1 for count in digit_counts.values() if count % 2 != 0)
    
    # A number can be rearranged to form a palindrome if at most one digit has an odd frequency
    return odd_count <= 1