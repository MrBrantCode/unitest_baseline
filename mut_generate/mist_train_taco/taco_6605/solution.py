"""
QUESTION:
# Description:

 Move all exclamation marks to the end of the sentence

# Examples

```
remove("Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!!"
remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"
```
"""

def move_exclamation_marks_to_end(s: str) -> str:
    return s.replace('!', '') + s.count('!') * '!'