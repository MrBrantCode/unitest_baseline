"""
QUESTION:
Create a function `eliminate_apple` that takes two lists as input: `fruit_names` and `fruit_properties`. The function should return two new lists, excluding the entries where the fruit name is 'apple', while maintaining the mapping between fruit names and their properties. The function should be optimized for large input lists.
"""

def eliminate_apple(fruit_names, fruit_properties):
    # new lists to keep entries excluding 'apple'
    new_fruit_names = [fruit for fruit in fruit_names if fruit != 'apple']
    new_fruit_properties = [prop for fruit, prop in zip(fruit_names, fruit_properties) if fruit != 'apple']
    
    return new_fruit_names, new_fruit_properties