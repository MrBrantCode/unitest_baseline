"""
QUESTION:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are: 

2332
110011
54322345

For a given number ```num```, write a function which returns the number of numerical palindromes within each number. For this kata, single digit numbers will NOT be considered numerical palindromes. 

Return "Not valid" if the input is not an integer or is less than 0.

```
palindrome(5) => 0
palindrome(1221) => 2 
palindrome(141221001) => 5  
palindrome(1294) => 0
palindrome("1221") => "Not valid"

```

```Haskell
In Haskell, return a Maybe Int with Nothing for negative numbers.
```

Other Kata in this Series:
Numerical Palindrome #1
Numerical Palindrome #1.5
Numerical Palindrome #2
Numerical Palindrome #3
Numerical Palindrome #3.5
Numerical Palindrome #4
Numerical Palindrome #5
"""

def count_numerical_palindromes(num):
    # Check if the input is a valid integer and non-negative
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    
    # Convert the number to a string for easier manipulation
    s = str(num)
    
    # Initialize a counter for numerical palindromes
    palindrome_count = 0
    
    # Iterate over all possible lengths of substrings (from 2 to the length of the string)
    for n in range(2, len(s) + 1):
        # Iterate over all possible starting positions for substrings of length n
        for i in range(len(s) - n + 1):
            # Extract the substring and its reverse
            substring = s[i:i + n]
            reversed_substring = substring[::-1]
            
            # Check if the substring is a palindrome
            if substring == reversed_substring:
                palindrome_count += 1
    
    return palindrome_count