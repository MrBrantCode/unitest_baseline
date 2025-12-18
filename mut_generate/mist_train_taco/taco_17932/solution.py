"""
QUESTION:
Write a function that takes a number or a string and gives back the number of **permutations without repetitions** that can generated using all of its element.; more on permutations [here](https://en.wikipedia.org/wiki/Permutation).

For example, starting with:
```
1
45
115
"abc"
```

You could respectively generate:
```
1
45,54
115,151,511
"abc","acb","bac","bca","cab","cba"
```

So you should have, in turn:
```python
perms(1)==1
perms(45)==2
perms(115)==3
perms("abc")==6
```
"""

from math import factorial
from functools import reduce
from operator import mul
from collections import Counter

def count_permutations(inp):
    # Convert the input to a string to handle both numbers and strings uniformly
    inp_str = str(inp)
    
    # Calculate the total number of permutations if all characters were unique
    total_permutations = factorial(len(inp_str))
    
    # Calculate the factorial of the counts of each character to account for repetitions
    repetitions_factor = reduce(mul, map(factorial, Counter(inp_str).values()), 1)
    
    # The number of unique permutations is the total permutations divided by the repetitions factor
    return total_permutations // repetitions_factor