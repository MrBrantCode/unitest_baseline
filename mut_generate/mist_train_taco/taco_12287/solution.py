"""
QUESTION:
Mike and Joe are fratboys that love beer and games that involve drinking. They play the following game: Mike chugs one beer, then Joe chugs 2 beers, then Mike chugs 3 beers, then Joe chugs 4 beers, and so on. Once someone can't drink what he is supposed to drink, he loses.

Mike can chug at most A beers in total (otherwise he would pass out), while Joe can chug at most B beers in total. Who will win the game? 

Write the function ```game(A,B)``` that returns the winner, ```"Mike"``` or ```"Joe"``` accordingly, for any given integer values of A and B.

Note: If either Mike or Joe cannot drink at least 1 beer, return the string  ```"Non-drinkers can't play"```.
"""

def determine_game_winner(max_mike: int, max_joe: int) -> str:
    if max_mike < 1 or max_joe < 1:
        return "Non-drinkers can't play"
    
    rounds_mike = int(max_mike ** 0.5)
    rounds_joe = int((-1 + (1 + 4 * max_joe) ** 0.5) // 2)
    
    if rounds_mike <= rounds_joe:
        return "Joe"
    else:
        return "Mike"