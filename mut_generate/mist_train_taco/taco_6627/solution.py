"""
QUESTION:
The marketing team is spending way too much time typing in hashtags.   
Let's help them with our own Hashtag Generator!

Here's the deal:

- It must start with a hashtag (`#`).
- All words must have their first letter capitalized.
- If the final result is longer than 140 chars it must return `false`.
- If the input or the result is an empty string it must return `false`.


## Examples

```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```
"""

def generate_hashtag(s: str) -> str | bool:
    # Initialize the output with a hashtag
    output = '#'
    
    # Iterate over each word in the input string, split by spaces
    for word in s.split():
        # Capitalize the first letter of each word and append to the output
        output += word.capitalize()
    
    # Check if the input string is empty or the output exceeds 140 characters
    if len(s) == 0 or len(output) > 140:
        return False
    
    # Return the generated hashtag
    return output