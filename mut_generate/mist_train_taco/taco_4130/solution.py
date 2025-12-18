"""
QUESTION:
IT City company developing computer games decided to upgrade its way to reward its employees. Now it looks the following way. After a new game release users start buying it actively, and the company tracks the number of sales with precision to each transaction. Every time when the next number of sales is not divisible by any number from 2 to 10 every developer of this game gets a small bonus.

A game designer Petya knows that the company is just about to release a new game that was partly developed by him. On the basis of his experience he predicts that n people will buy the game during the first month. Now Petya wants to determine how many times he will get the bonus. Help him to know it.


-----Input-----

The only line of the input contains one integer n (1 ≤ n ≤ 10^18) — the prediction on the number of people who will buy the game.


-----Output-----

Output one integer showing how many numbers from 1 to n are not divisible by any number from 2 to 10.


-----Examples-----
Input
12

Output
2
"""

def calculate_bonus_count(n: int) -> int:
    """
    Calculate the number of times a developer will get a bonus based on the number of game sales.

    The bonus is given when the number of sales is not divisible by any number from 2 to 10.

    Parameters:
    n (int): The prediction on the number of people who will buy the game.

    Returns:
    int: The number of times the developer will get the bonus.
    """
    # Using the principle of Inclusion-Exclusion to count numbers divisible by 2 to 10
    res = (n // 2 + n // 3 + n // 5 + n // 7
           - n // 6 - n // 10 - n // 14 - n // 15 - n // 21 - n // 35
           + n // 30 + n // 42 + n // 70 + n // 105
           - n // 210)
    
    # The number of numbers from 1 to n that are not divisible by any number from 2 to 10
    return n - res