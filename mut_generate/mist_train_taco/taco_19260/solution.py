"""
QUESTION:
If we alternate the vowels and consonants in the string `"have"`, we get the following list, arranged alphabetically:
`['ahev', 'aveh', 'ehav', 'evah', 'vahe', 'veha']`. These are the only possibilities in which vowels and consonants are alternated. The first element, `ahev`, is alphabetically lowest. 

Given a string:
* alternate the vowels and consonants and return the lexicographically lowest element in the list
* If any two or more vowels or consonants must follow each other, return `"failed"`
* if the number of vowels and consonants are equal, the first letter of the result must be a vowel.

Examples: 

```Haskell
solve("codewars") = "failed". However you alternate vowels and consonants, two consonants must follow each other
solve("oruder") = "edorur"
solve("orudere") = "ederoru". This is the only option that allows you to alternate vowels & consonants.
```

```if c:
In C, return an allocated string even if the response is "failed".
```

Vowels will be any of "aeiou". Input will be a lowercase string, no spaces. See test cases for more examples. 

Good luck!

If you like this Kata, please try: 

[Consonant value](https://www.codewars.com/kata/59c633e7dcc4053512000073)

[Alternate capitalization](https://www.codewars.com/kata/59cfc000aeb2844d16000075)
"""

def alternate_vowels_consonants(s: str) -> str:
    vowels = sorted((c for c in s if c in 'aeiou'))
    consonants = sorted((c for c in s if c not in 'aeiou'))
    
    # Determine which list is longer
    part1, part2 = sorted((vowels, consonants), key=len, reverse=True)
    
    # Ensure both lists have the same length by appending an empty string to the shorter one
    part2.append('')
    
    # Check if alternation is possible
    if len(part1) > len(part2):
        return 'failed'
    
    # Join the characters from part1 and part2 alternately
    result = ''.join((a + b for a, b in zip(part1, part2)))
    
    return result