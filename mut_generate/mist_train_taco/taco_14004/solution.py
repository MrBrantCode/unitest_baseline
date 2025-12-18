"""
QUESTION:
We have had record hot temperatures this summer. To avoid heat stroke, you decided to buy a quantity of drinking water at the nearby supermarket. Two types of bottled water, 1 and 0.5 liter, are on sale at respective prices there. You have a definite quantity in your mind, but are willing to buy a quantity larger than that if: no combination of these bottles meets the quantity, or, the total price becomes lower.

Given the prices for each bottle of water and the total quantity needed, make a program to seek the lowest price to buy greater than or equal to the quantity required.



Input

The input is given in the following format.


$A$ $B$ $X$


The first line provides the prices for a 1-liter bottle $A$ ($1\leq A \leq 1000$), 500-milliliter bottle $B$ ($1 \leq B \leq 1000$), and the total water quantity needed $X$ ($1 \leq X \leq 20000$). All these values are given as integers, and the quantity of water in milliliters.

Output

Output the total price.

Examples

Input

180 100 2400


Output

460


Input

200 90 2018


Output

450
"""

def calculate_lowest_price(A: int, B: int, X: int) -> int:
    if B * 2 <= A:
        # If two 500ml bottles are cheaper or equal to one 1L bottle
        ans = B * (X // 500 + bool(X % 500))
    else:
        # Calculate the cost using 1L bottles and the remaining with 500ml bottles
        ans = A * (X // 1000) + min(B * (X % 1000 // 500 + bool(X % 1000 % 500)), A * bool(X % 1000))
    return ans