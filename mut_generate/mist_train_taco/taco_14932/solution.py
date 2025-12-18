"""
QUESTION:
In this Kata, you will be given a string of numbers in sequence and your task will be to return the missing number. If there is no number
missing or there is an error in the sequence, return `-1`.

For example:
```Haskell
missing("123567") = 4 
missing("899091939495") = 92
missing("9899101102") = 100
missing("599600601602") = -1 -- no number missing
missing("8990919395") = -1 -- error in sequence. Both 92 and 94 missing.
```
The sequence will always be in ascending order.

More examples in the test cases. 

Good luck!
"""

def find_missing_number(seq: str) -> int:
    for digits in range(1, len(seq) // 2 + 1):
        my_seq = last = seq[:digits]
        n = int(my_seq)
        missing = None
        while len(my_seq) < len(seq):
            n += 1
            my_seq += str(n)
            if not seq.startswith(my_seq):
                if missing is None:
                    missing = n
                    my_seq = last
                else:
                    break
            else:
                last = my_seq
        if my_seq == seq and missing is not None:
            return missing
    return -1