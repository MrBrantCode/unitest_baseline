"""
QUESTION:
There is an N-car train.
You are given an integer i. Find the value of j such that the following statement is true: "the i-th car from the front of the train is the j-th car from the back."

-----Constraints-----
 - 1 \leq N \leq 100
 - 1 \leq i \leq N

-----Input-----
Input is given from Standard Input in the following format:
N i

-----Output-----
Print the answer.

-----Sample Input-----
4 2

-----Sample Output-----
3

The second car from the front of a 4-car train is the third car from the back.
"""

def find_car_position_from_back(N: int, i: int) -> int:
    """
    Finds the position of the i-th car from the front of the train as the j-th car from the back.

    Parameters:
    - N (int): The total number of cars in the train.
    - i (int): The position of the car from the front.

    Returns:
    - int: The position of the car from the back.
    """
    return N - i + 1