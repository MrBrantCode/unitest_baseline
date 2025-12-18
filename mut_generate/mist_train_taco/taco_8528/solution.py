"""
QUESTION:
Serval is fighting with a monster.
The health of the monster is H.
In one attack, Serval can decrease the monster's health by A.
There is no other way to decrease the monster's health.
Serval wins when the monster's health becomes 0 or below.
Find the number of attacks Serval needs to make before winning.

-----Constraints-----
 - 1 \leq H \leq 10^4
 - 1 \leq A \leq 10^4
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
H A

-----Output-----
Print the number of attacks Serval needs to make before winning.

-----Sample Input-----
10 4

-----Sample Output-----
3

 - After one attack, the monster's health will be 6.
 - After two attacks, the monster's health will be 2.
 - After three attacks, the monster's health will be -2.
Thus, Serval needs to make three attacks to win.
"""

def calculate_attacks_needed(H: int, A: int) -> int:
    """
    Calculate the number of attacks Serval needs to make to reduce the monster's health to 0 or below.

    Parameters:
    - H (int): The initial health of the monster.
    - A (int): The amount of health the monster loses per attack.

    Returns:
    - int: The number of attacks needed.
    """
    attacks_needed = 0
    while H > 0:
        H -= A
        attacks_needed += 1
    return attacks_needed