"""
QUESTION:
There are some animals in a garden. Each of them is a crane with two legs or a turtle with four legs.
Takahashi says: "there are X animals in total in the garden, and they have Y legs in total." Determine whether there is a combination of numbers of cranes and turtles in which this statement is correct.

-----Constraints-----
 - 1 \leq X \leq 100
 - 1 \leq Y \leq 100
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
X Y

-----Output-----
If there is a combination of numbers of cranes and turtles in which the statement is correct, print Yes; otherwise, print No.

-----Sample Input-----
3 8

-----Sample Output-----
Yes

The statement "there are 3 animals in total in the garden, and they have 8 legs in total" is correct if there are two cranes and one turtle. Thus, there is a combination of numbers of cranes and turtles in which the statement is correct.
"""

def is_valid_animal_combination(X: int, Y: int) -> str:
    """
    Determines whether there is a valid combination of cranes and turtles
    that satisfies the given total number of animals and legs.

    Parameters:
    - X (int): Total number of animals.
    - Y (int): Total number of legs.

    Returns:
    - str: 'Yes' if a valid combination exists, otherwise 'No'.
    """
    if Y % 2 == 0 and Y >= 2 * X and Y <= 4 * X:
        return 'Yes'
    else:
        return 'No'