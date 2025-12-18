"""
QUESTION:
Timothy (age: 16) really likes to smoke. Unfortunately, he is too young to buy his own cigarettes and that's why he has to be extremely efficient in smoking.

It's now your task to create a function that calculates how many cigarettes Timothy can smoke out of the given amounts of `bars` and `boxes`:

- a bar has 10 boxes of cigarettes,
- a box has 18 cigarettes,
- out of 5 stubs (cigarettes ends) Timothy is able to roll a new one,
- of course the self made cigarettes also have an end which can be used to create a new one...

Please note that Timothy never starts smoking cigarettes that aren't "full size" so the amount of smoked cigarettes is always an integer.
"""

def calculate_total_cigarettes(bars, boxes):
    # Calculate the total number of cigarettes from bars and boxes
    total_cigarettes = (bars * 10 + boxes) * 18
    
    # Initialize the count of smoked cigarettes
    smoked_cigarettes = 0
    
    # Initialize the count of stubs
    stubs = 0
    
    # While there are cigarettes to smoke
    while total_cigarettes > 0:
        # Smoke all available cigarettes
        smoked_cigarettes += total_cigarettes
        stubs += total_cigarettes
        
        # Calculate new cigarettes from stubs
        total_cigarettes = stubs // 5
        stubs = stubs % 5
    
    return smoked_cigarettes