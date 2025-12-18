"""
QUESTION:
You want to build a standard house of cards, but you don't know how many cards you will need. Write a program which will count the minimal number of cards according to the number of floors you want to have. For example, if you want a one floor house, you will need 7 of them (two pairs of two cards on the base floor, one horizontal card and one pair to get the first floor). Here you can see which kind of house of cards I mean:
http://www.wikihow.com/Build-a-Tower-of-Cards

## Note about floors:
This kata uses the British numbering system for building floors. If you want your house of cards to have a first floor, it needs a ground floor and then a first floor above that.

### Details (Ruby & JavaScript & Python & R)
The input must be an integer greater than 0, for other input raise an error.

### Details (Haskell)
The input must be an integer greater than 0, for other input return `Nothing`.
"""

def calculate_house_of_cards(n):
    """
    Calculate the minimal number of cards needed to build a house of cards with `n` floors.

    Parameters:
    n (int): The number of floors in the house of cards. Must be greater than 0.

    Returns:
    int: The minimal number of cards needed.

    Raises:
    ValueError: If `n` is less than or equal to 0.
    """
    if n <= 0:
        raise ValueError("The number of floors must be greater than 0.")
    
    return (n + 1) * n // 2 + (n + 2) * (n + 1)