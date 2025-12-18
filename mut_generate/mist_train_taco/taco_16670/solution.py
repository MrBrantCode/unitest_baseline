"""
QUESTION:
Takahashi likes the sound when he buys a drink from a vending machine.
That sound can be heard by spending A yen (the currency of Japan) each time.
Takahashi has B yen. He will hear the sound as many times as he can with that money, but at most C times, as he would be satisfied at that time.
How many times will he hear the sound?

-----Constraints-----
 - All values in input are integers.
 - 1 \leq A, B, C \leq 100

-----Input-----
Input is given from Standard Input in the following format:
A B C

-----Output-----
Print the number of times Takahashi will hear his favorite sound.

-----Sample Input-----
2 11 4

-----Sample Output-----
4

Since he has not less than 8 yen, he will hear the sound four times and be satisfied.
"""

def calculate_sound_times(A: int, B: int, C: int) -> int:
    """
    Calculate the number of times Takahashi will hear the sound based on the given constraints.

    Parameters:
    - A (int): The cost in yen to hear the sound once.
    - B (int): The total amount of yen Takahashi has.
    - C (int): The maximum number of times Takahashi will hear the sound before getting satisfied.

    Returns:
    - int: The number of times Takahashi will hear the sound.
    """
    return min(B // A, C)