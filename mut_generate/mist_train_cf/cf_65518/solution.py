"""
QUESTION:
Write a function `calculate_horses` to calculate the number of horses, given the number of cows and the ratio of cows to horses. The number of cows is six times the number of horses. The function should take two parameters: `cows` and `ratio`, and return the number of horses. The ratio of cows to horses is fixed at 6, so it can be hardcoded in the function.
"""

def calculate_horses(cows, ratio):
    # To find the number of horses (h), we divide the number of cows by the ratio
    horses = cows / ratio
    return horses