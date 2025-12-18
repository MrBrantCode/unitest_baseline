"""
QUESTION:
Roma is programmer and he likes memes about IT,  
Maxim is chemist and he likes memes about chemistry,  
Danik is designer and he likes memes about design,  
and Vlad likes all other memes.

___

You will be given a meme (string), and your task is to identify its category, and send it to the right receiver: `IT - 'Roma'`, `chemistry - 'Maxim'`, `design - 'Danik'`, or `other - 'Vlad'`.

IT meme has letters `b, u, g`.  
Chemistry meme has letters `b, o, o, m`.  
Design meme has letters `e, d, i, t, s`.  
If there is more than 1 possible answer, the earliest match should be chosen.

**Note:** letters are case-insensetive and should come in the order specified above.

___

## Examples:

(Matching letters are surrounded by curly braces for readability.)

```
this is programmer meme {b}ecause it has b{ug}
this is also program{bu}r meme {g}ecause it has needed key word
this is {ed}s{i}gner meme cause i{t} ha{s} key word

this could {b}e chemistry meme b{u}t our{g}Gey word 'boom' is too late
    instead of
this could {b}e chemistry meme but {o}ur gey w{o}rd 'boo{m}' is too late
```
"""

import re
from itertools import accumulate

def categorize_meme(meme: str) -> str:
    """
    Categorizes a meme and determines the appropriate receiver based on the content.

    Parameters:
    meme (str): The content of the meme.

    Returns:
    str: The name of the person who should receive the meme.
    """
    patterns = [
        (re.compile('.*'.join('bug'), flags=re.I), 'Roma'),
        (re.compile('.*'.join('boom'), flags=re.I), 'Maxim'),
        (re.compile('.*'.join('edits'), flags=re.I), 'Danik')
    ]
    
    return next((who for m in accumulate(meme) for (pattern, who) in patterns if pattern.search(m)), 'Vlad')