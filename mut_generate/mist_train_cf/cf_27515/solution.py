"""
QUESTION:
Write a function `sortMangaTitles` that takes a list of strings representing Japanese manga titles and returns a new list with the titles sorted in lexicographical order based on the Latin characters only, ignoring case. Non-Latin characters, such as kanji, hiragana, and katakana, should be ignored during sorting. The original list should not be modified.
"""

from typing import List

def sort_manga_titles(titles: List[str]) -> List[str]:
    def remove_special_characters(title: str) -> str:
        return ''.join(filter(str.isalpha, title)).lower()

    return sorted(titles, key=lambda title: remove_special_characters(title))