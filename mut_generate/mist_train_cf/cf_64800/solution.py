"""
QUESTION:
Create a function named `calculate_weight` that calculates the total weight of groceries in a shopping basket. The function should take a list of dictionaries as an argument, where each dictionary represents an item with keys for "item", "weight" or "volume", and "category". The categories can be "fruits_vegetables", "beverages", or "canned_goods". The function should return the total weight in kilograms, considering that 1 liter of liquid is approximately 1 kg and 1 gram is 0.001 kg. If an item is missing a weight or volume, or if the category is unknown, the function should return an error message.
"""

def calculate_weight(groceries):
    total_weight = 0
    for item in groceries:
        category = item['category']
        if category == 'fruits_vegetables':
            weight = item.get('weight', None)
            if weight:
                total_weight += weight
            else:
                return 'Error: Weight Not Found for Item: {}'.format(item['item'])
        elif category == 'beverages':
            volume = item.get('volume', None)
            if volume:
                total_weight += volume
            else:
                return 'Error: Volume Not Found for Item: {}'.format(item['item'])
        elif category == 'canned_goods':
            weight = item.get('weight', None)
            if weight:
                total_weight += weight * 0.001
            else:
                return 'Error: Weight Not Found for Item: {}'.format(item['item'])
        else:
           return 'Error: Unknown Category: {}'.format(category)
    return total_weight