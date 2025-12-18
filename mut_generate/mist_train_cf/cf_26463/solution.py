"""
QUESTION:
Create a function `extract_winning_numbers(text: str) -> List[List[int]]` that takes a string `text` as input and returns a list of lists of integers. The function should find all occurrences of the phrase "ВЫИГРЫШНЫЕ НОМЕРА" in the input text, extract the space-separated integers immediately following this phrase, and return these integers as a list of lists, where each inner list contains the numbers following a single occurrence of the phrase.
"""

from typing import List

def extract_winning_numbers(text: str) -> List[List[int]]:
    winning_numbers = []
    start_index = text.find("ВЫИГРЫШНЫЕ НОМЕРА")
    while start_index != -1:
        end_index = text.find("\n", start_index)
        numbers_str = text[start_index + len("ВЫИГРЫШНЫЕ НОМЕРА"):end_index].strip()
        numbers = list(map(int, numbers_str.split()))
        winning_numbers.append(numbers)
        start_index = text.find("ВЫИГРЫШНЫЕ НОМЕРА", end_index)
    return winning_numbers