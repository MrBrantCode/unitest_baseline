"""
QUESTION:
Write a function named `chocolateWeights` that takes two parameters, `totalWeight` and `amountEaten`, both of which are positive integers. `totalWeight` is the combined weight of chocolates in two boxes, and `amountEaten` is the amount of chocolates eaten from the larger box. After eating `amountEaten` kilograms of chocolates from the larger box, the weight ratio of the chocolates in the larger box to the smaller box becomes 4:3. The function should return the original weights of the chocolates in the larger and smaller boxes as a tuple (largerBox, smallerBox) before any chocolates were eaten.
"""

def chocolateWeights(totalWeight, amountEaten):
    # The total weight after eating some chocolates
    postEatWeight = totalWeight - amountEaten
    # The combined weight of 7 parts after eating some chocolates
    combinedWeight = postEatWeight / 7
    # The weights of the larger and smaller boxes after eating some chocolates
    largerBoxPostEat = combinedWeight * 4
    smallerBoxPostEat = combinedWeight * 3
    # The original weight of the larger box, before eating some chocolates
    largerBox = largerBoxPostEat + amountEaten
    # The original weight of the smaller box is same as its weight after eating some chocolates,
    # as no chocolates were eaten from the smaller box
    smallerBox = smallerBoxPostEat
    return round(largerBox), round(smallerBox)