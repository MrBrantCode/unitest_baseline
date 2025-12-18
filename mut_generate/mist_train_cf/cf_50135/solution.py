"""
QUESTION:
Write a function `elephants_in_zoo(total_animals, zebra_more)` that calculates the number of elephants in a zoo given the total number of animals and the number of extra zebras beyond three times the number of elephants. The function should return the number of elephants if the input data is valid and the result is an integer; otherwise, it should return an error message. The total number of animals and the number of extra zebras are non-negative integers, and the number of extra zebras is less than the total number of animals.
"""

def elephants_in_zoo(total_animals, zebra_more):
    if not (isinstance(total_animals, int) and isinstance(zebra_more, int)) or total_animals < 1 or zebra_more < 1 or zebra_more > total_animals:
        return "Invalid input data"
      
    elephants = (total_animals - zebra_more) / 4

    if elephants.is_integer():
        return int(elephants)
    return "The result is fractional which is not possible for the number of elephants in a zoo"