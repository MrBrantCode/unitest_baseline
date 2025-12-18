"""
QUESTION:
Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.

Class ID Ship ClassB or bBattleShipC or cCruiserD or dDestroyerF or fFrigate

-----Input-----

The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains a character. 

-----Output-----
For each test case, display the Ship Class depending on ID, in a new line.

-----Constraints-----
- 1 ≤ T ≤ 1000

-----Example-----
Input

3 
B
c
D

Output
BattleShip
Cruiser
Destroyer
"""

def get_ship_class(letter_id: str) -> str:
    if letter_id in ['B', 'b']:
        return 'BattleShip'
    elif letter_id in ['C', 'c']:
        return 'Cruiser'
    elif letter_id in ['D', 'd']:
        return 'Destroyer'
    elif letter_id in ['F', 'f']:
        return 'Frigate'
    else:
        return 'Unknown'  # In case of an unexpected input