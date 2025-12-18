"""
QUESTION:
Write a function called `categorize_sentiments` that takes a list of integers representing sentiment scores as input, where scores range from 1 to 100. The function should categorize the scores into three levels: mildly positive (70-79), moderately positive (80-89), and highly positive (90-100), and return a dictionary with the count of scores in each category. The input list can contain scores outside of these ranges, but they should be ignored in the categorization process.
"""

def categorize_sentiments(sentiments):
    counts = {'mildly positive': 0, 'moderately positive': 0, 'highly positive': 0}
    for s in sentiments:
        if s >= 70 and s <= 79:
            counts['mildly positive'] += 1
        elif s >= 80 and s <= 89:
            counts['moderately positive'] += 1
        elif s >= 90 and s <= 100:
            counts['highly positive'] += 1
    return counts