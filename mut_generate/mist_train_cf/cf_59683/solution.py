"""
QUESTION:
Write a function `listed_numbers(l1: list, l2: list)` that takes two lists of integers as input and returns a dictionary containing three lists. The first list, 'evens', should contain all even integers from both input lists, sorted in reverse order. The second list, 'pos_odds_l1', should contain all positive odd integers from the first list, sorted in reverse order. The third list, 'neg_odds_l2', should contain all negative odd integers from the second list, sorted in reverse order. Implement auxiliary functions `merge_and_sort(m: list, n: list)`, `filter_negatives(o: list)`, and `filter_positives(o: list)` to aid in the solution. 

Note that the function should only include strictly even integers from both lists and not include any non-even integers in the 'evens' list. Also, the 'pos_odds_l1' list should only include positive odd integers from the first list and the 'neg_odds_l2' list should only include negative odd integers from the second list.
"""

def listed_numbers(l1: list, l2: list):
    """Return a dict with a list of strictly even integers from a pair of lists and separate single lists of positive odds from the first list and negative odds from the second. All lists must be amalgamated and ordered in reverse numerical order."""
    
    def merge_and_sort(m: list, n: list):
        """Merge and sort two lists in reverse order."""
        return sorted(m + n, reverse=True)

    def filter_negatives(o: list):
        """Filter negative numbers from a list and return them in reverse order."""
        return sorted([num for num in o if num < 0 and num % 2 != 0], reverse=True)

    def filter_positives(o: list):
        """Filter positive numbers from a list and return them in reverse order."""
        return sorted([num for num in o if num > 0 and num % 2 != 0], reverse=True)

    evens = merge_and_sort([num for num in l1 if num % 2 == 0], [num for num in l2 if num % 2 == 0])
    pos_odds_l1 = filter_positives(l1)
    neg_odds_l2 = filter_negatives(l2)
    
    return {'evens': evens, 'pos_odds_l1': pos_odds_l1, 'neg_odds_l2': neg_odds_l2}