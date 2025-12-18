"""
QUESTION:
Create a function named `peculiar_sum` that takes a list of strings containing only digits. The function should return a list of strings. Each string in the returned list should have the format "the quantity of odd components Xn the strXng X of the Xnput.", where X is the count of odd digits in the corresponding input string and X replaces all instances of 'i' in the string.
"""

def peculiar_sum(lst):
    result = []
    for i, s in enumerate(lst):
        num_odds = sum(int(c) % 2 for c in s)
        st = "the quantity of odd components {}n the str{}ng {} of the {}nput.".format(num_odds, num_odds, i+1, i+1)
        result.append(st)
    return result