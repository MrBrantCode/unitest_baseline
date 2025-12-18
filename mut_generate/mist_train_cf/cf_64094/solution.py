"""
QUESTION:
Write a function classify_fruits that takes a dictionary of fruits and their nutritional information as input. The dictionary should contain fruit names as keys and another dictionary with keys 'vitamin_c_mg_per_100g', 'fiber_g_per_100g', and 'origin' as values. The function should group the fruits into three lists: Group A (fruits with at least 50mg of vitamin C per 100g and originating from Asia), Group B (fruits with at least 2g of fiber per 100g and originating from the Americas), and Group C (all other fruits). Return the three groups of fruits.
"""

def classify_fruits(fruits):
    """
    Classify fruits into three groups based on their nutritional information and origin.
    
    Parameters:
    fruits (dict): A dictionary containing fruit names as keys and another dictionary 
                   with keys 'vitamin_c_mg_per_100g', 'fiber_g_per_100g', and 'origin' as values.
    
    Returns:
    tuple: A tuple of three lists representing Group A, Group B, and Group C fruits.
    """
    group_a, group_b, group_c = [], [], []
    
    for fruit, info in fruits.items():
        if info['vitamin_c_mg_per_100g'] >= 50 and 'Asia' in info['origin']:
            group_a.append(fruit)
        elif info['fiber_g_per_100g'] >= 2.0 and 'America' in info['origin']:
            group_b.append(fruit)
        else:
            group_c.append(fruit)
    
    return group_a, group_b, group_c