"""
QUESTION:
Implement a function which behaves like the uniq command in UNIX.

It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance.

Example:

```
["a", "a", "b", "b", "c", "a", "b", "c"]  =>  ["a", "b", "c", "a", "b", "c"]
```
"""

from itertools import groupby

def remove_consecutive_duplicates(seq):
    """
    Removes consecutive duplicate elements from the input sequence.

    Parameters:
    seq (list or iterable): The input sequence from which consecutive duplicates will be removed.

    Returns:
    list: A list containing the elements of the input sequence with consecutive duplicates removed.
    """
    return [k for (k, _) in groupby(seq)]