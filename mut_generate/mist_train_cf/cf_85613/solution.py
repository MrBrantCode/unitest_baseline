"""
QUESTION:
Write a function named `calculate_special_tuples` that takes a list of integers as input. It should return a tuple of six elements: 
- the number of distinct positive even integers in the list
- the number of distinct negative even integers in the list
- the sum of squares of all distinct positive even integers in the list
- the sum of squares of all distinct negative even integers in the list
- the sum of cubes of all distinct odd integers in the list
- the product of all distinct odd integers in the list.
If there are no integers for the given conditions, return 0 for that condition.
"""

def calculate_special_tuples(lst):
    pos_evens, neg_evens, odds = set(), set(), set()
    pos_evens_squared_sum, neg_evens_squared_sum, odds_cubed_sum, odds_product = 0, 0, 0, 1
    
    for num in lst:
        if num:
            if num > 0:
                if num % 2 == 0:
                    if num not in pos_evens:
                        pos_evens.add(num)
                        pos_evens_squared_sum += num ** 2
                else:
                    if num not in odds:
                        odds.add(num)
                        odds_product *= num
                    odds_cubed_sum += num ** 3

            elif num < 0 and num % 2 == 0:
                if num not in neg_evens:
                    neg_evens.add(num)
                    neg_evens_squared_sum += num ** 2

    return len(pos_evens), len(neg_evens), pos_evens_squared_sum, neg_evens_squared_sum, odds_cubed_sum, odds_product