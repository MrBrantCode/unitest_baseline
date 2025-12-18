"""
QUESTION:
In input string ```word```(1 word):
* replace the vowel with the nearest left consonant.
* replace the consonant with the nearest right vowel.

P.S. To complete this task imagine the alphabet is a circle (connect the first and last element of the array in the mind). For example, 'a' replace with 'z', 'y' with 'a', etc.(see below)

For example:
```
'codewars' => 'enedazuu'
'cat' => 'ezu'
'abcdtuvwxyz' => 'zeeeutaaaaa'
```

It is preloaded: 

```
const alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
const consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'];
const vowels = ['a','e','i','o','u'];
```

P.S. You work with lowercase letters only.
"""

def replace_letters(word: str) -> str:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowels = ['a','e','i','o','u']
    
    def nearest_right_vowel(char):
        index = alphabet.index(char)
        while True:
            index = (index + 1) % len(alphabet)
            if alphabet[index] in vowels:
                return alphabet[index]
    
    def nearest_left_consonant(char):
        index = alphabet.index(char)
        while True:
            index = (index - 1) % len(alphabet)
            if alphabet[index] in consonants:
                return alphabet[index]
    
    result = []
    for char in word:
        if char in vowels:
            result.append(nearest_left_consonant(char))
        elif char in consonants:
            result.append(nearest_right_vowel(char))
    
    return ''.join(result)