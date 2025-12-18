"""
QUESTION:
The Spelling Bee bees are back...

# How many bees are in the beehive?

* bees can be facing UP, DOWN, LEFT, RIGHT, and now also _diagonally_ up/down/left/right
* bees can share parts of other bees



## Examples

Ex1
```
bee.bee     
.e..e..
.b..eeb
```
_Answer: 5_

Ex2
```
beee..     
eeb.e.
ebee.b
```
_Answer: 7_
"""

def count_bees_in_hive(hive):
    if not hive:
        return 0
    
    # Transpose the hive to get vertical sequences
    vertical_hive = list(zip(*hive))
    
    # Create padding to handle diagonal sequences
    padding = [None] * len(hive)
    
    # Generate forward and backward diagonal sequences
    forward_diagonals = [
        [n for n in l if n is not None]
        for l in zip(*(padding[i:] + list(row) + padding[:i] for i, row in enumerate(hive)))
    ]
    backward_diagonals = [
        [n for n in l if n is not None]
        for l in zip(*(padding[:i] + list(row) + padding[i:] for i, row in enumerate(hive)))
    ]
    
    # Combine all sequences
    all_sequences = hive + [''.join(row) for row in vertical_hive] + [''.join(row) for row in forward_diagonals] + [''.join(row) for row in backward_diagonals]
    
    # Flatten the sequences into a single string
    inline = '\n'.join(all_sequences)
    
    # Count occurrences of "bee" in both forward and reverse directions
    return (inline + inline[::-1]).count('bee')