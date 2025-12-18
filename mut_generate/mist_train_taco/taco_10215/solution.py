"""
QUESTION:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are: 

2332
110011
54322345

For this kata, single digit numbers will not be considered numerical palindromes. 

For a given number ```num```, write a function to test if the number contains a numerical palindrome or not and return a boolean (true if it does and false if does not). Return "Not valid" if the input is not an integer or is less than 0. 

Note: Palindromes should be found without permutating ```num```. 

```
palindrome(5) => false
palindrome(1221) => true
palindrome(141221001) => true
palindrome(1215) => true 
palindrome(1294) => false 
palindrome("109982") => "Not valid"
```
"""

def contains_numerical_palindrome(num):
    # Check if the input is a valid integer and non-negative
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    
    # Convert the number to a string for easier manipulation
    s = str(num)
    
    # Check for palindromes of length 2 or 3
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2]:
            return True
    
    # Check the last two digits for a palindrome
    return len(s) != 1 and s[-1] == s[-2]