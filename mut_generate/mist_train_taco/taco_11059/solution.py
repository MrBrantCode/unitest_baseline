"""
QUESTION:
Kate and Michael want to buy a pizza and share it. Depending on the price of the pizza, they are going to divide the costs:

* If the pizza is less than €5,- Michael invites Kate, so Michael pays the full price.
* Otherwise Kate will contribute 1/3 of the price, but no more than €10 (she's broke :-) and Michael pays the rest.

How much is Michael going to pay? Calculate the amount with two decimals, if necessary.
"""

def calculate_michael_payment(cost: float) -> float:
    if cost < 5:
        return round(cost, 2)
    else:
        kate_contribution = min(cost / 3, 10)
        michael_payment = cost - kate_contribution
        return round(michael_payment, 2)