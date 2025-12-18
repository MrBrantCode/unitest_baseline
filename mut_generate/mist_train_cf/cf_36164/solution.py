"""
QUESTION:
Write a function named `count_algorithm_categories` that takes a list of strings representing different algorithm categories and returns a dictionary containing the count of each category present in the input list. The categories to be considered are 'general', 'hard_example_mining', 'aggregation', 'multi_task_learning', and 'unseen_task_detect'. 

The input list will have a length between 1 and 100. The function should ignore any categories not present in the input list.
"""

from typing import List, Dict

def entrance(categories: List[str]) -> Dict[str, int]:
    category_counts = {
        'general': 0,
        'hard_example_mining': 0,
        'aggregation': 0,
        'multi_task_learning': 0,
        'unseen_task_detect': 0
    }

    for category in categories:
        if category in category_counts:
            category_counts[category] += 1

    return {category: count for category, count in category_counts.items() if count > 0}