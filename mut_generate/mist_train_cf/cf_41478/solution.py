"""
QUESTION:
Write a function `categorizeShortcuts(shortcuts)` that takes a list of strings representing keyboard shortcuts as input and returns a tuple of two lists. The first list should contain all the single-character shortcuts, and the second list should contain all the combination shortcuts. A keyboard shortcut is either a single character or a combination of modifier keys (Ctrl, Alt, Shift) and characters. The input list will only contain valid keyboard shortcuts in the specified format.
"""

from typing import List, Tuple

def categorizeShortcuts(shortcuts: List[str]) -> Tuple[List[str], List[str]]:
    single_char_shortcuts = []
    combination_shortcuts = []

    for shortcut in shortcuts:
        if '+' in shortcut:
            combination_shortcuts.append(shortcut)
        else:
            single_char_shortcuts.append(shortcut)

    return single_char_shortcuts, combination_shortcuts