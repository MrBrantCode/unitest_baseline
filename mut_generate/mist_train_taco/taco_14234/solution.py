"""
QUESTION:
# Introduction

There is a war and nobody knows - the alphabet war!  
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

# Task

Write a function that accepts `fight` string consists of only small letters and return who wins the fight. When the left side wins return `Left side wins!`, when the right side wins return `Right side wins!`, in other case return `Let's fight again!`.

The left side letters and their power:
```
 w - 4
 p - 3
 b - 2
 s - 1
```
The right side letters and their power:
```
 m - 4
 q - 3
 d - 2
 z - 1
```
The other letters don't have power and are only victims.

# Example

# Alphabet war Collection



Alphavet war 


Alphabet war - airstrike - letters massacre


Alphabet wars - reinforces massacre


Alphabet wars - nuclear strike


Alphabet war - Wo lo loooooo priests join the war
"""

def determine_winner(fight: str) -> str:
    # Define the power of each letter for both sides
    power = {
        'w': 4, 'p': 3, 'b': 2, 's': 1,  # Left side letters
        'm': -4, 'q': -3, 'd': -2, 'z': -1  # Right side letters
    }
    
    # Calculate the total power of the fight
    total_power = sum(power.get(c, 0) for c in fight)
    
    # Determine the result based on the total power
    if total_power > 0:
        return "Left side wins!"
    elif total_power < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"