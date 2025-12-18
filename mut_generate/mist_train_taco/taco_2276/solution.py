"""
QUESTION:
Given two strings, the first being a random string and the second being the same as the first, but with three added characters somewhere in the string (three same characters),

Write a function that returns the added character

### E.g

```
string1 = "hello"
string2 = "aaahello"

// => 'a'
```

The above is just an example; the characters could be anywhere in the string and string2 is actually **shuffled**.

### Another example

```
string1 = "abcde"
string2 = "2db2a2ec"

// => '2'
```

Note that the added character could also exist in the original string


```
string1 = "aabbcc"
string2 = "aacccbbcc"

// => 'c'
```

You can assume that string2 will aways be larger than string1, and there will always be three added characters in string2.

```if:c
Write the function `added_char()` that takes two strings and return the added character as described above.
```

```if:javascript
Write the function `addedChar()` that takes two strings and return the added character as described above.
```
"""

from collections import Counter

def addedChar(string1, string2):
    # Count the characters in both strings
    count1 = Counter(string1)
    count2 = Counter(string2)
    
    # Subtract the counts of string1 from string2
    diff = count2 - count1
    
    # The added character will be the first (and only) element in the difference
    return next(iter(diff.elements()))