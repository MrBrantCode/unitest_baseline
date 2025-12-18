"""
QUESTION:
The chef has a recipe he wishes to use for his guests,
but the recipe will make far more food than he can serve to the guests.
The chef therefore would like to make a reduced version of the recipe which has the same ratios of ingredients, but makes less food.
The chef, however, does not like fractions.
The original recipe contains only whole numbers of ingredients,
and the chef wants the reduced recipe to only contain whole numbers of ingredients as well.
Help the chef determine how much of each ingredient to use in order to make as little food as possible.

------ Input ------ 

Input will begin with an integer T, the number of test cases.
Each test case consists of a single line.
The line begins with a positive integer N, the number of ingredients.
N integers follow, each indicating the quantity of a particular ingredient that is used.

------ Output ------ 

For each test case, output exactly N space-separated integers on a line,
giving the quantity of each ingredient that the chef should use in order to make as little food as possible.

------ Constraints ------ 

T ≤ 100 

2 ≤ N ≤ 50

All ingredient quantities are between 1 and 1000, inclusive.

----- Sample Input 1 ------ 
3
2 4 4
3 2 3 4
4 3 15 9 6
----- Sample Output 1 ------ 
1 1
2 3 4
1 5 3 2
"""

def reduce_recipe(test_cases):
    def find_hcf(numbers):
        hcf = 1
        for i in range(2, min(numbers) + 1):
            if all(num % i == 0 for num in numbers):
                hcf = i
        return hcf

    reduced_recipes = []
    
    for case in test_cases:
        N = case[0]
        ingredients = case[1:]
        hcf = find_hcf(ingredients)
        reduced_ingredients = [ingredient // hcf for ingredient in ingredients]
        reduced_recipes.append(reduced_ingredients)
    
    return reduced_recipes