"""
QUESTION:
Write a function `listed_numbers(l1: list, l2: list)` that takes two lists of integers as input and returns a dictionary with three keys: 'evens', 'pos_odds_l1', and 'neg_odds_l2'. 

The 'evens' key should map to a list of all even numbers from both input lists, sorted in descending order. The 'pos_odds_l1' key should map to a list of all positive odd numbers from the first input list, and the 'neg_odds_l2' key should map to a list of all negative odd numbers from the second input list. 

The function should not assume any specific ordering of the input lists and should handle duplicate numbers. The function should also handle empty input lists.
"""

def listed_numbers(l1: list, l2: list):
    """
    Return a dict with a list of strictly even integers from a pair of lists and separate single lists
    of positive odds from the first list and negative odds from the second. 
    All lists must be amalgamated and ordered in reverse numerical order.
    """

    # Implement an auxiliary function for merging and ordering arrays
    def merge_and_sort(n: list, m: list):
        return sorted(n + m, reverse=True)
        
    # Implement an auxiliary function for filtering negative numbers from an array
    def filter_negatives(o: list):
        return [i for i in o if i < 0]
    
    # Implement an auxiliary function for filtering positive numbers from an array
    def filter_positives(o: list):
        return [i for i in o if i > 0]

    evens = []
    for num in merge_and_sort(l1, l2):
        if num % 2 == 0:
            evens.append(num)

    pos_odds_l1 = filter_positives([num for num in l1 if num % 2 != 0])
    neg_odds_l2 = filter_negatives([num for num in l2 if num % 2 != 0])
    
    return {'evens': evens, 'pos_odds_l1': pos_odds_l1, 'neg_odds_l2': neg_odds_l2}