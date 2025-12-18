"""
QUESTION:
Create a function `getNextInts` that takes a string of comma-separated integers, sorts them in ascending order, and returns a list of the next integers in the sequence up to 100. The input string will contain only comma-separated integers with no spaces or other non-numeric characters. The function should return an empty list if the maximum integer in the input string is 100 or greater.
"""

def getNextInts(strInts):
    """
    This function takes a string of comma-separated integers, sorts them in ascending order, 
    and returns a list of the next integers in the sequence up to 100.

    Args:
        strInts (str): A string of comma-separated integers.

    Returns:
        list: A list of the next integers in the sequence up to 100.
    """

    # Convert string into list of integers and sort the list
    lstInts = sorted([int(x) for x in strInts.split(',')])

    # Find the maximum in the list
    maxInt = max(lstInts)

    # If the maximum integer is 100 or greater, return an empty list
    if maxInt >= 100:
        return []

    # Generate the next integers in sequence up to 100
    return list(range(maxInt+1, 101))