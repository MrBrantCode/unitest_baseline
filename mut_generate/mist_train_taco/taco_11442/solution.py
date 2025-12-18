"""
QUESTION:
Consider the following series:

`1, 2, 4, 8, 16, 22, 26, 38, 62, 74, 102, 104, 108, 116, 122`

It is generated as follows:

* For single digit integers, add the number to itself to get the next element.
* For other integers, multiply all the non-zero digits and add the result to the original number to get the next element.

For example: `16 + (6 * 1) = 22` and `104 + (4 * 1) = 108`. 

Let's begin the same series with a seed value of `3` instead of `1`:

`3, 6, 12, 14, 18, 26, 38, 62, 74, 102, 104, 108, 116, 122`

Notice that the two sequences converge at `26` and are identical therefter. We will call the series seeded by a value of `1` the "base series" and the other series the "test series". 

You will be given a seed value for the test series and your task will be to return the number of integers that have to be generated in the test series before it converges to the base series. In the case above:
```Python
convergence(3) = 5, the length of [3, 6, 12, 14, 18]. 
```  

Good luck!

If you like this Kata, please try:

[Simple Prime Streaming](https://www.codewars.com/kata/5a908da30025e995880000e3)

[Unique digit sequence](https://www.codewars.com/kata/599688d0e2800dda4e0001b0)

[Divisor harmony](https://www.codewars.com/kata/59bf97cd4f98a8b1cd00007e)
"""

from operator import mul
from functools import reduce

def genSequence(n):
    yield n
    while True:
        n += reduce(mul, [int(d) for d in str(n) if d != '0']) if n > 9 else n
        yield n

def extract(seq, v):
    return sorted(seq).index(v)

def convergence_length(seed):
    (gen1, genN) = (genSequence(1), genSequence(seed))
    (seq1, seqN) = ({next(gen1)}, {next(genN)})
    while True:
        (a, b) = (next(gen1), next(genN))
        seq1.add(a)
        seqN.add(b)
        if a in seqN:
            return extract(seqN, a)
        if b in seq1:
            return extract(seqN, b)