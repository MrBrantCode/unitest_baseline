"""
QUESTION:
You are given an input string.

For each symbol in the string if it's the first character occurrence, replace it with a '1', else replace it with the amount of times you've already seen it...
      
But will your code be **performant enough**?

___

## Examples:

```
input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"
```

There might be some non-ascii characters in the string.

~~~if:java
Note: there will be no int domain overflow (character occurrences will be less than 2 billion).
~~~
~~~if:c
(this does not apply to the C language translation)
~~~
"""

def numericals(s: str) -> str:
    """
    Replace each character in the input string with a '1' if it's the first occurrence,
    otherwise replace it with the number of times it has already been seen.

    Parameters:
    s (str): The input string to be processed.

    Returns:
    str: The resulting string after processing.
    """
    char_count = {}
    result = []
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        result.append(str(char_count[char]))
    
    return ''.join(result)