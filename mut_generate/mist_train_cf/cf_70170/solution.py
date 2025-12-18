"""
QUESTION:
Implement the `kelly_criterion` function, which calculates the optimal bet size as a fraction of the bankroll given the probability of winning and the payoff odds. The function should take in three parameters: `bankroll`, `probability_of_winning`, and `payoff_odds`.
"""

def kelly_criterion(bankroll, probability_of_winning, payoff_odds):
    return (probability_of_winning * payoff_odds - (1 - probability_of_winning)) / (payoff_odds - 1)