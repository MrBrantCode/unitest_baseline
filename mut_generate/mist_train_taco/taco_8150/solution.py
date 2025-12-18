"""
QUESTION:
Ataru Oafoot of Aizu Gakuen University High School decided to play with a slot machine.

When you insert a medal on this machine, three reels will start spinning and each reel will stop automatically. In a normal game (normal game), 3 medals are inserted, and when the symbols are aligned, the following medals are obtained according to the symbols.

<image>



A special service will be started depending on how the patterns are aligned. A big bonus starts when you have 3 of 7 symbols, and you can play 5 bonus games. Also, when you have 3 BAR symbols, the regular bonus will start and you can play 3 bonus games.

If you have 3 star symbols, the free game will start and you will not be able to get medals, but you can start the next game without inserting medals.

During the bonus game, if you insert 2 medals per game, you will automatically get 3 grape patterns and 15 medals.

Oafoot started playing on the machine with 100 medals. After playing for a while, it ended in a normal game. How many medals did you have left?

Create a program that inputs play information and outputs the number of medals left at hand. The play information is given as the number of big bonuses b, the number of regular bonuses r, the number of grapes aligned during a normal game g, the number of cherries aligned c, the number of stars aligned s, and the total number of games t.

Note that t includes the number of bonus games. Also, medals will not disappear in the middle of the game.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a zero line. Each dataset is given in the following format:


b r g c s t


b, r, g, c, and s are integers greater than or equal to 0 and less than 200, and t is an integer less than or equal to 1000.

The number of datasets does not exceed 120.

Output

For each input dataset, the number of medals remaining at hand is output on one line.

Example

Input

3 2 30 3 26 226
9 0 18 3 20 118
5 5 12 2 15 203
7 4 19 2 22 197
7 4 24 4 17 209
0 0 0 0 0 0


Output

127
793
414
629
617
"""

def calculate_remaining_medals(b: int, r: int, g: int, c: int, s: int, t: int) -> int:
    # Initial number of medals
    ans = 100
    
    # Calculate medals from big bonuses
    ans += (15 - 2) * (5 * b) + (15 - 3) * b
    t -= 6 * b
    
    # Calculate medals from regular bonuses
    ans += (15 - 2) * (3 * r) + (15 - 3) * r
    t -= 4 * r
    
    # Calculate medals from grapes aligned
    ans += (7 - 3) * g
    t -= g
    
    # Calculate medals from cherries aligned
    ans += (2 - 3) * c
    t -= c
    
    # Subtract games played with stars
    t -= s
    
    # Calculate medals from remaining normal games
    ans += (0 - 3) * t
    
    return ans