"""
QUESTION:
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top card is still on top.

For example, faro shuffling the list
```python
['ace', 'two', 'three', 'four', 'five', 'six']
```
gives
```python
['ace', 'four', 'two', 'five', 'three', 'six' ]
```

If 8 perfect faro shuffles are performed on a deck of 52 playing cards, the deck is restored to its original order.

Write a function that inputs an integer n and returns an integer representing the number of faro shuffles it takes to restore a deck of n cards to its original order.

Assume n is an even number between 2 and 2000.
"""

def calculate_faro_shuffle_cycles(n):
    """
    Calculate the number of faro shuffles required to restore a deck of n cards to its original order.

    Parameters:
    n (int): The number of cards in the deck, where n is an even number between 2 and 2000.

    Returns:
    int: The number of faro shuffles required to restore the deck to its original order.
    """
    (x, cnt) = (2, 1)
    while x != 1 and n > 3:
        cnt += 1
        x = x * 2 % (n - 1)
    return cnt