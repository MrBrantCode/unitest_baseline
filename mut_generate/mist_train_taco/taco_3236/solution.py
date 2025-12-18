"""
QUESTION:
# Task
 Consider a string of lowercase Latin letters and space characters (" "). 
 
 First, rearrange the letters in each word `alphabetically`. 
 
 And then rearrange the words in ascending order of the sum of their characters' `ASCII` values. 
 
 If two or more words have the same `ASCII` value, rearrange them by their length in ascending order; If their length still equals to each other, rearrange them `alphabetically`.
 
 Finally, return the result.

# Example

 For `s = "batman is bruce wayne"`, the result should be `"is bceru aenwy aamntb"`.
``` 
After rearranging the letters the string turns into
"aamntb is bceru aenwy".
The ASCII values of each word are: [627, 220, 529, 548].
After sorting the words the following string is obtained:
"is bceru aenwy aamntb" (with ASCII values of [220, 529, 548, 627]).```

 For `s = "peter parker is spiderman"`, the result should be `"is eeprt aekprr adeimnprs"`

 `(ASCII values: [220, 554, 645, 963])`

# Input/Output


 - `[input]` string `s`

  A string of lowercase words. Each word is separated by exactly one space character.


 - `[output]` a string
"""

def revamp_string(s: str) -> str:
    # Step 1: Rearrange the letters in each word alphabetically
    words = [''.join(sorted(word)) for word in s.split()]
    
    # Step 2: Sort the words based on the sum of their ASCII values, length, and alphabetically
    words.sort(key=lambda word: (sum(map(ord, word)), len(word), word))
    
    # Step 3: Join the sorted words back into a single string
    return ' '.join(words)