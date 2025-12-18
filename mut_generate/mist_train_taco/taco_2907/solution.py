"""
QUESTION:
You are given an initial 2-value array (x). You will use this to calculate a score.

If both values in (x) are numbers, the score is the sum of the two. If only one is a number, the score is that number. If neither is a number, return 'Void!'.


Once you have your score, you must return an array of arrays. Each sub array will be the same as (x) and the number of sub arrays should be equal to the score.

For example:

if (x) == ['a', 3]  you should return [['a', 3], ['a', 3], ['a', 3]].
"""

def calculate_score_and_explode(x):
    # Calculate the score based on the conditions
    numbers = [v for v in x if isinstance(v, int)]
    if len(numbers) == 2:
        score = sum(numbers)
    elif len(numbers) == 1:
        score = numbers[0]
    else:
        return 'Void!'
    
    # Return the list of sub arrays based on the score
    return [x] * score