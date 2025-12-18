"""
QUESTION:
Write a function that replaces 'two', 'too' and 'to' with the number '2'. Even if the sound is found mid word (like in octopus) or not in lowercase grandma still thinks that should be replaced with a 2. Bless her.

```text
'I love to text' becomes 'I love 2 text'
'see you tomorrow' becomes 'see you 2morrow'
'look at that octopus' becomes 'look at that oc2pus'
```

Note that 'too' should become '2', not '2o'
"""

import re

def replace_words_with_two(txt: str) -> str:
    """
    Replaces occurrences of 'two', 'too', and 'to' (case-insensitive) with '2' in the given text.

    Parameters:
    txt (str): The input text to be processed.

    Returns:
    str: The processed text with all specified words replaced by '2'.
    """
    return re.sub('(two|too|to)', '2', txt, flags=re.I)