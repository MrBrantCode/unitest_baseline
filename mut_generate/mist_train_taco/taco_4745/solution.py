"""
QUESTION:
Variation of this nice kata, the war has expanded and become dirtier and meaner; both even and odd numbers will fight with their pointy `1`s. And negative integers are coming into play as well, with, ça va sans dire, a negative contribution (think of them as spies or saboteurs).

Again, three possible outcomes: `odds win`, `evens win` and `tie`.

Examples:

```python
bits_war([1,5,12]) => "odds win" #1+101 vs 1100, 3 vs 2
bits_war([7,-3,20]) => "evens win" #111-11 vs 10100, 3-2 vs 2
bits_war([7,-3,-2,6]) => "tie" #111-11 vs -1+110, 3-2 vs -1+2
```
"""

def determine_bits_war_winner(numbers):
    odd_score = 0
    even_score = 0
    
    for number in numbers:
        bit_count = bin(abs(number)).count('1')
        if number % 2 == 0:
            even_score += bit_count if number > 0 else -bit_count
        else:
            odd_score += bit_count if number > 0 else -bit_count
    
    if odd_score > even_score:
        return "odds win"
    elif even_score > odd_score:
        return "evens win"
    else:
        return "tie"