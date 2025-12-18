"""
QUESTION:
Write a function `numWaterBottles` that takes three integers `numBottles`, `numExchange`, and `numFriends` as input, where `numBottles` is the initial number of full water bottles, `numExchange` is the number of empty water bottles required to exchange for one full water bottle, and `numFriends` is the number of friends who will drink and return empty bottles. The function should return the maximum number of water bottles that can be drunk, given the constraints that 1 <= `numBottles` <= 100, 2 <= `numExchange` <= 100, and 1 <= `numFriends` <= 10.
"""

def numWaterBottles(numBottles: int, numExchange: int, numFriends: int) -> int:
    total = numBottles  # total bottles drank
    empty = numBottles  # first, we have numBottles empty bottles after drinking

    # while we have enough to exchange or enough to give to friends
    while empty >= numExchange or empty >= numFriends:
        exchange_bottles = empty // numExchange  # how many bottles we can get from exchanging
        friend_bottles = empty // numFriends  # how many bottles we can give to friends

        # how many bottles left after exchanging and giving to friends
        left = empty - (exchange_bottles * numExchange + friend_bottles * numFriends)
        
        # the total bottles drank is increased by exchange_bottles and friend_bottles
        total += exchange_bottles + friend_bottles

        # update the empty bottles
        empty = exchange_bottles + left

    return total