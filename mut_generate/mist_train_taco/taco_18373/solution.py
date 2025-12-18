"""
QUESTION:
# Task

John has an important number, and he doesn't want others to see it.

He decided to encrypt the number, using the following steps:
```
His number is always a non strict increasing sequence
ie. "123"

He converted each digit into English words.
ie. "123"--> "ONETWOTHREE"

And then, rearrange the letters randomly.
ie. "ONETWOTHREE" --> "TTONWOHREEE"
```

John felt that his number were safe in doing so. In fact, such encryption can be easily decrypted :(

Given the encrypted string `s`, your task is to decrypt it, return the original number in string format.

Note, You can assume that the input string `s` is always valid; It contains only uppercase Letters; The decrypted numbers are arranged in ascending order; The leading zeros are allowed.


# Example

For `s = "ONE"`, the output should be `1`.

For `s = "EON"`, the output should be `1` too.

For `s = "ONETWO"`, the output should be `12`.

For `s = "OONETW"`, the output should be `12` too.

For `s = "ONETWOTHREE"`, the output should be `123`.

For `s = "TTONWOHREEE"`, the output should be `123` too.
"""

from collections import Counter

EXECUTIONS_ORDER = [
    ('Z', Counter('ZERO'), '0'),
    ('W', Counter('TWO'), '2'),
    ('U', Counter('FOUR'), '4'),
    ('X', Counter('SIX'), '6'),
    ('G', Counter('EIGHT'), '8'),
    ('O', Counter('ONE'), '1'),
    ('H', Counter('THREE'), '3'),
    ('F', Counter('FIVE'), '5'),
    ('V', Counter('SEVEN'), '7'),
    ('I', Counter('NINE'), '9')
]

def decrypt_encrypted_number(s: str) -> str:
    ans = []
    count = Counter(s)
    executions = iter(EXECUTIONS_ORDER)
    
    while count:
        c, word_count, value = next(executions)
        ans.extend([value] * count[c])
        for _ in range(count[c]):
            count -= word_count
    
    return ''.join(sorted(ans))