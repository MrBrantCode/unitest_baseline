"""
QUESTION:
One suggestion to build a satisfactory password is to start with a memorable phrase or sentence and make a password by extracting the first letter of each word. 

Even better is to replace some of those letters with numbers (e.g., the letter `O` can be replaced with the number `0`):

* instead of including `i` or `I` put the number `1` in the password;
* instead of including `o` or `O` put the number `0` in the password;
* instead of including `s` or `S` put the number `5` in the password.


## Examples:
```
"Give me liberty or give me death"  --> "Gml0gmd"
"Keep Calm and Carry On"            --> "KCaC0"
```
"""

def generate_password(phrase: str) -> str:
    SWAP = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}
    
    # Extract the first letter of each word and apply the swap rules
    password_chars = [SWAP.get(word[0], word[0]) for word in phrase.split()]
    
    # Join the characters to form the final password
    return ''.join(password_chars)