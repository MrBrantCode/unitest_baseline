"""
QUESTION:
Your task is to generate the Fibonacci sequence to `n` places, with each alternating value as `"skip"`. For example:

`"1 skip 2 skip 5 skip 13 skip 34"`

Return the result as a string

You can presume that `n` is always a positive integer between (and including) 1 and 64.
"""

def generate_skiponacci_sequence(n: int) -> str:
    if n < 1 or n > 64:
        raise ValueError("n must be a positive integer between 1 and 64")
    
    if n == 1:
        return "1"
    
    sequence = ["1"]
    num = 1
    prv = 0
    
    for i in range(1, n):
        new = num + prv
        prv = num
        num = new
        if i % 2 == 0:
            sequence.append(str(num))
        else:
            sequence.append("skip")
    
    return ' '.join(sequence)