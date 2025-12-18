"""
QUESTION:
A sweet little monster Om Nom loves candies very much. One day he found himself in a rather tricky situation that required him to think a bit in order to enjoy candies the most. Would you succeed with the same task if you were on his place? [Image] 

One day, when he came to his friend Evan, Om Nom didn't find him at home but he found two bags with candies. The first was full of blue candies and the second bag was full of red candies. Om Nom knows that each red candy weighs W_{r} grams and each blue candy weighs W_{b} grams. Eating a single red candy gives Om Nom H_{r} joy units and eating a single blue candy gives Om Nom H_{b} joy units.

Candies are the most important thing in the world, but on the other hand overeating is not good. Om Nom knows if he eats more than C grams of candies, he will get sick. Om Nom thinks that it isn't proper to leave candy leftovers, so he can only eat a whole candy. Om Nom is a great mathematician and he quickly determined how many candies of what type he should eat in order to get the maximum number of joy units. Can you repeat his achievement? You can assume that each bag contains more candies that Om Nom can eat.


-----Input-----

The single line contains five integers C, H_{r}, H_{b}, W_{r}, W_{b} (1 ≤ C, H_{r}, H_{b}, W_{r}, W_{b} ≤ 10^9).


-----Output-----

Print a single integer — the maximum number of joy units that Om Nom can get.


-----Examples-----
Input
10 3 5 2 3

Output
16



-----Note-----

In the sample test Om Nom can eat two candies of each type and thus get 16 joy units.
"""

def maximize_joy(C, H_r, H_b, W_r, W_b):
    result = 0
    
    # Check if iterating over red candies is more efficient
    if W_r * W_r >= C:
        i = 0
        while W_r * i <= C:
            j = (C - W_r * i) // W_b
            result = max(result, H_r * i + H_b * j)
            i += 1
        return result
    
    # Check if iterating over blue candies is more efficient
    if W_b * W_b >= C:
        i = 0
        while W_b * i <= C:
            j = (C - W_b * i) // W_r
            result = max(result, H_b * i + H_r * j)
            i += 1
        return result
    
    # Compare the joy per gram of red and blue candies
    joy_per_gram_r = H_r / W_r
    joy_per_gram_b = H_b / W_b
    
    if joy_per_gram_b < joy_per_gram_r:
        i = 0
        while i * i <= C:
            j = (C - W_b * i) // W_r
            result = max(result, H_b * i + H_r * j)
            i += 1
    else:
        i = 0
        while i * i <= C:
            j = (C - W_r * i) // W_b
            result = max(result, H_r * i + H_b * j)
            i += 1
    
    return result