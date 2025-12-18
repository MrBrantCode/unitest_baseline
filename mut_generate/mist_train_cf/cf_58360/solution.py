"""
QUESTION:
Construct a function named `manage_basket` that takes a list of dictionaries representing a basket of groceries and a maximum weight limit as arguments. Each dictionary in the list contains the name of a grocery item and its weight. The function should return a list of dictionaries representing the groceries that fit within the weight limit and a list of dictionaries representing the groceries that need to be removed to stay within the weight limit. If the total weight of the groceries exceeds the maximum limit, the function should suggest removing items starting from the heaviest one until the total weight is under the limit.
"""

def manage_basket(basket, limit):
    # Sort the basket in descending order by weight
    basket.sort(key=lambda x:x['weight'], reverse=True)
    
    total_weight = sum(x['weight'] for x in basket)
    items_to_remove = []
    
    # Keep removing the heaviest item until the total weight is less than the limit
    while total_weight > limit:
        item = basket.pop(0)
        total_weight -= item['weight']
        items_to_remove.append(item)
        
    return basket, items_to_remove