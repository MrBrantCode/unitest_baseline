"""
QUESTION:
Calculate the total points a dieter has after dieting for a certain number of days. The dieter consumes calories[i] calories on the i-th day. 

Given the parameters:
- `calories` (array): daily calorie consumption
- `k` (integer): consecutive sequence of days to evaluate calorie consumption
- `lower` (integer): lower bound for calorie consumption evaluation
- `upper` (integer): upper bound for calorie consumption evaluation
- `G` (integer): target points to reach
- `extraDays` (integer): additional days to diet if target points not reached
- `extraCalories` (integer): calories consumed each day during extra dieting days

The function should calculate the total points after dieting for `calories.length + extraDays` days, following these rules:
- lose 1 point if total calories in k days < lower
- gain 1 point if total calories in k days > upper
- no change in points otherwise

Constraints:
- 1 <= k <= calories.length <= 10^5
- 0 <= calories[i] <= 20000
- 0 <= lower <= upper
- -10^5 <= G <= 10^5
- 0 <= extraDays <= 10^5
- 0 <= extraCalories <= 20000
"""

def diet_plan_performance(calories, k, lower, upper, G, extraDays, extraCalories):
    """
    Calculate the total points a dieter has after dieting for a certain number of days.

    Args:
    calories (array): daily calorie consumption
    k (integer): consecutive sequence of days to evaluate calorie consumption
    lower (integer): lower bound for calorie consumption evaluation
    upper (integer): upper bound for calorie consumption evaluation
    G (integer): target points to reach
    extraDays (integer): additional days to diet if target points not reached
    extraCalories (integer): calories consumed each day during extra dieting days

    Returns:
    integer: total points after dieting for calories.length + extraDays days
    """

    points = 0
    # Calculate the total calories for the first 'k' days
    T = sum(calories[:k])
    
    # Check the points for the first 'k' days
    if T < lower:
        points -= 1
    elif T > upper:
        points += 1
    
    # Calculate the points for the remaining days
    for i in range(k, len(calories)):
        T = T - calories[i-k] + calories[i]
        if T < lower:
            points -= 1
        elif T > upper:
            points += 1
    
    # Add extra days if the target points are not reached
    if points < G:
        for _ in range(extraDays):
            points += 1 if extraCalories > upper else -1 if extraCalories < lower else 0
    
    return points