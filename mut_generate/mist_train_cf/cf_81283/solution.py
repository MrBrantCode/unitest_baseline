"""
QUESTION:
Write a function `calculate_investment(stocks, investment, returns)` that determines all the possible distributions of investment among the given stocks to maximize the return. The function should take a list of stock return rates `stocks`, the total invested amount `investment`, and the total return `returns` as input. The investment for each stock should be a multiple of $100, and the investment does not have to span across all stock types.
"""

def calculate_investment(stocks, investment, returns):
    sequences = [[(0, 0)] for _ in range(len(stocks) + 1)]
    for i in range(1, len(stocks) + 1):
        for previous in sequences[i - 1]:
            additional = 0
            while True:
                additional += 1
                money = previous[0] + additional * 100
                gain = previous[1] + additional * stocks[i - 1]
                if money > investment or gain > returns:
                    break
                if money <= investment and gain <= returns:
                    sequences[i].append((money, gain))
    paths = []
    for sequence in sequences[-1]:
        if sequence == (investment, returns):
            paths.append(sequence)
    return paths