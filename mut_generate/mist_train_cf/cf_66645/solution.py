"""
QUESTION:
Implement a function named `fruit_distribution` that takes six parameters: 
- `s`: a list of strings representing the quantity of various fruits in a basket, 
- `n`: the total number of fruits in the basket, 
- `fruits`: a list of fruit types, 
- `servings`: a dictionary containing the servings each fruit can provide, 
- `nutrition`: a dictionary containing the nutritional value of each fruit, 
- `time_limit`: an integer representing a time limit within which the fruits must be distributed.

Return a dictionary reflecting servings of each type of fruit not mentioned in the list, within the time constraint. The function should prioritize fruits based on their nutritional value and not distribute a fruit if a recipient already has that type of fruit. The result should be a dictionary that only includes fruits with non-zero servings.
"""

def fruit_distribution(s, n, fruits, servings, nutrition, time_limit):
    food_dist = {}
    for fruit in s:
        fruit_name = fruit.split(' ')[1]
        fruit_qty = int(fruit.split(' ')[0])
        if fruit_qty < servings[fruit_name]: 
            time_limit -= fruit_qty
        else: 
            fruit_qty = servings[fruit_name]
            time_limit -= servings[fruit_name]

        if time_limit < 0: 
            break  

        if fruit_name in food_dist:
            food_dist[fruit_name] += fruit_qty
        else:
            food_dist[fruit_name] = fruit_qty

    remaining_fruits = set(fruits) - set(food_dist.keys())
    for fruit in sorted(remaining_fruits, key=lambda x: nutrition[x], reverse=True):
        if time_limit <= 0: 
            break  

        if time_limit >= servings[fruit]:
            food_dist[fruit] = servings[fruit]
            time_limit -= servings[fruit]
        else:
            food_dist[fruit] = time_limit
            time_limit = 0

    return {k:v for k, v in food_dist.items() if v > 0 and k not in [i.split(' ')[1] for i in s]}