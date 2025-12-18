"""
QUESTION:
There is a train going from Station A to Station B that costs X yen (the currency of Japan).
Also, there is a bus going from Station B to Station C that costs Y yen.
Joisino got a special ticket. With this ticket, she can take the bus for half the fare if she travels from Station A to Station B by train and then travels from Station B to Station C by bus.
How much does it cost to travel from Station A to Station C if she uses this ticket?

-----Constraints-----
 - 1 \leq X,Y \leq 100
 - Y is an even number.
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
X Y

-----Output-----
If it costs x yen to travel from Station A to Station C, print x.

-----Sample Input-----
81 58

-----Sample Output-----
110

 - The train fare is 81 yen.
 - The train fare is 58 ⁄ 2=29 yen with the 50% discount.
Thus, it costs 110 yen to travel from Station A to Station C.
"""

def calculate_total_travel_cost(train_fare: int, bus_fare: int) -> int:
    """
    Calculate the total cost to travel from Station A to Station C, considering a special ticket discount for the bus fare.

    Parameters:
    - train_fare (int): The cost of the train from Station A to Station B.
    - bus_fare (int): The cost of the bus from Station B to Station C.

    Returns:
    - total_cost (int): The total cost to travel from Station A to Station C.
    """
    total_cost = train_fare + (bus_fare // 2)
    return total_cost