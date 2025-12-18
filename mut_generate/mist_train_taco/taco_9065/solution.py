"""
QUESTION:
In this Kata, you will check if it is possible to convert a string to a palindrome by changing one character. 

For instance:
```Haskell
solve ("abbx") = True, because we can convert 'x' to 'a' and get a palindrome. 
solve ("abba") = False, because we cannot get a palindrome by changing any character. 
solve ("abcba") = True. We can change the middle character. 
solve ("aa") = False 
solve ("ab") = True
```

Good luck!

Please also try [Single Character Palindromes](https://www.codewars.com/kata/5a2c22271f7f709eaa0005d3)
"""

def can_convert_to_palindrome(s: str) -> bool:
    # Count the number of mismatches when comparing the string with its reverse
    mismatches = sum((s[i] != s[-1 - i] for i in range(len(s) // 2)))
    
    # Check if the number of mismatches is exactly one or if there are no mismatches and the string length is odd
    return mismatches == 1 or (not mismatches and len(s) % 2)