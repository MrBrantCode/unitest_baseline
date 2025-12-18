"""
QUESTION:
### Longest Palindrome

Find the length of the longest substring in the given string `s` that is the same in reverse.        

As an example, if the input was “I like racecars that go fast”, the substring (`racecar`) length would be `7`. 

If the length of the input string is `0`, the return value must be `0`. 

### Example:
```
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
```
"""

def find_longest_palindrome_length(s: str) -> int:
    if not s:
        return 0
    
    maxPal = 0
    for i in range(len(s)):
        # Check for odd length palindromes
        tmpPal = 1
        left, right = i - 1, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            tmpPal += 2
            left -= 1
            right += 1
        maxPal = max(maxPal, tmpPal)
        
        # Check for even length palindromes
        tmpPal = 0
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            tmpPal += 2
            left -= 1
            right += 1
        maxPal = max(maxPal, tmpPal)
    
    return maxPal