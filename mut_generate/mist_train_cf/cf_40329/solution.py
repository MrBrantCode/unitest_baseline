"""
QUESTION:
Given a list of integers representing people's heights in a line, determine the number of people visible from the front. A person is visible if there is no one taller standing in front of them. The list contains 1 to 10^5 integers, each representing a height between 1 and 10^9. Write a function `visible_people_count` that takes this list and returns the count of visible people.
"""

from typing import List

def visible_people_count(h: List[int]) -> int:
    visible_count = 0
    max_height = 0

    for height in h:
        if height > max_height:
            visible_count += 1
            max_height = height

    return visible_count