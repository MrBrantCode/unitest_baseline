"""
QUESTION:
Create a function `unusual_addition(lst)` that takes a list of strings containing numerical figures as input. For each string, calculate the sum of odd digits and its square root, then replace the index 'i' in the phrase "the number of odd elements i in the string i of the input" with the sum of odd digits and 'i' with the square root of the sum of odd digits. Also, calculate the cumulative sum of all odd digits from all strings. Return a list containing the modified phrases and the cumulative sum of all odd digits from each string.
"""

def unusual_addition(lst):
    result = []
    total = 0
    for i in range(len(lst)):
        sum_odds = sum([int(c) for c in lst[i] if int(c) % 2 == 1])
        total += sum_odds
        result.append("the number of odd elements %d in the string %d of the input" % (sum_odds, round(sum_odds**0.5)))
        result.append(total)
    return result