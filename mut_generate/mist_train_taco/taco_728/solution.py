"""
QUESTION:
Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too. 

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25... 

Complete the beeramid function to return the number of **complete** levels of a beer can pyramid you can make, given the parameters of: 

1) your referral bonus, and

2) the price of a beer can

For example:
"""

def calculate_complete_beeramid_levels(referral_bonus, beer_price):
    # Calculate the total number of beers that can be bought with the referral bonus
    total_beers = referral_bonus // beer_price
    
    # Initialize the level counter and the number of beers required for the current level
    levels = 0
    
    # Loop to determine the number of complete levels
    while total_beers >= (levels + 1) ** 2:
        levels += 1
        total_beers -= levels ** 2
    
    return levels