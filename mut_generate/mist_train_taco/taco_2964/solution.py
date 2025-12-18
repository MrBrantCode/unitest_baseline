"""
QUESTION:
You've arrived at a carnival and head straight for the duck shooting tent. Why wouldn't you?

You will be given a set amount of ammo, and an aim rating of between 1 and 0. No your aim is not always perfect - hey maybe someone fiddled with the sights on the gun...

Anyway your task is to calculate how many successful shots you will be able to make given the available ammo and your aim score, then return a string representing the pool of ducks, with those ducks shot marked with 'X' and those that survived left unchanged. You will always shoot left to right.

Example of start and end duck string with two successful shots:

Start ---> |~~~~~22~2~~~~~|

**Bang!! Bang!!**

End  --->  |~~~~~XX~2~~~~~|

All inputs will be correct type and never empty.
"""

def simulate_duck_shooting(ammo: int, aim: float, ducks: str) -> str:
    """
    Simulates a duck shooting game given the amount of ammo, aim rating, and the initial pool of ducks.

    Parameters:
    - ammo (int): The amount of ammunition available.
    - aim (float): The aim rating between 0 and 1.
    - ducks (str): The string representing the pool of ducks.

    Returns:
    - str: The pool of ducks after the shooting, with successful shots marked as 'X'.
    """
    successful_shots = int(ammo * aim)
    return ducks.replace('2', 'X', successful_shots)