"""
QUESTION:
We have a long seat of width X centimeters.
There are many people who wants to sit here. A person sitting on the seat will always occupy an interval of length Y centimeters.
We would like to seat as many people as possible, but they are all very shy, and there must be a gap of length at least Z centimeters between two people, and between the end of the seat and a person.
At most how many people can sit on the seat?

-----Constraints-----
 - All input values are integers.
 - 1 \leq X, Y, Z \leq 10^5
 - Y+2Z \leq X

-----Input-----
Input is given from Standard Input in the following format:
X Y Z

-----Output-----
Print the answer.

-----Sample Input-----
13 3 1

-----Sample Output-----
3

There is just enough room for three, as shown below:
Figure
"""

def max_people_on_seat(X: int, Y: int, Z: int) -> int:
    """
    Calculate the maximum number of people that can sit on a seat of width X centimeters,
    given that each person occupies an interval of length Y centimeters and there must be
    a gap of at least Z centimeters between two people and between the end of the seat and a person.

    Parameters:
    - X (int): The width of the seat in centimeters.
    - Y (int): The length of the interval a person occupies in centimeters.
    - Z (int): The minimum gap required between two people and between the end of the seat and a person in centimeters.

    Returns:
    - int: The maximum number of people that can sit on the seat.
    """
    return (X - Z) // (Y + Z)