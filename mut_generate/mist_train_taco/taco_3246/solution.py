"""
QUESTION:
A soldier wants to buy w bananas in the shop. He has to pay k dollars for the first banana, 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana). 

He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?


-----Input-----

The first line contains three positive integers k, n, w (1  ≤  k, w  ≤  1000, 0 ≤ n ≤ 10^9), the cost of the first banana, initial number of dollars the soldier has and number of bananas he wants. 


-----Output-----

Output one integer — the amount of dollars that the soldier must borrow from his friend. If he doesn't have to borrow money, output 0.


-----Examples-----
Input
3 17 4

Output
13
"""

def calculate_borrowed_amount(k: int, n: int, w: int) -> int:
    # Calculate the total cost of w bananas
    total_cost = sum(i * k for i in range(1, w + 1))
    
    # Calculate the amount of money to borrow
    borrowed_amount = total_cost - n
    
    # If the borrowed amount is negative or zero, return 0
    return max(borrowed_amount, 0)