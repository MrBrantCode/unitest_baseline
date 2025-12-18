"""
QUESTION:
Create a function named `fruit_distribution` that takes four parameters: `s` (total number of items in the basket), `n` (the day on which the items were picked), `items` (a list of strings representing the count of diverse fruits and non-fruit items), and `fruits` (a list of strings containing only fruits). The function should return two dictionaries, one with the count of each non-listed fruit and the other with counts of non-fruit items, or 'Error' if the total number of items is less than the sum of all items in the lists. If the items were picked on an odd day, the count of fruits should be increased by 10%. The dictionaries should only contain items with a non-zero count.
"""

def entance(s,n, items, fruits):
    from collections import defaultdict
    fruit_dict = dict()
    non_fruit_dict = dict()
    total_items = 0

    for item in items:
        name, quantity = item.split()
        quantity = int(quantity)
        total_items += quantity
        
        if name in fruits:
            fruit_dict[name] = quantity if n % 2 == 0 else int(quantity*1.1)
        else:
            non_fruit_dict[name] = quantity
    
    if total_items > s:
        return 'Error'
        
    return {key: value for key, value in fruit_dict.items() if value != 0}, {key: value for key, value in non_fruit_dict.items() if value != 0}