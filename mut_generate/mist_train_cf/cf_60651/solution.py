"""
QUESTION:
Develop a Python function `search_substr_positions(text, substr)` that searches for all occurrences of a specific character subset (`substr`) within a provided text fragment (`text`) and returns their positions if the characters in the subset appear in the same sequence. The function should be optimized to handle large text fragments efficiently.
"""

def search_substr_positions(text, substr):
    start = 0
    positions = []
    while start < len(text):
        pos = text.find(substr, start)
        if pos != -1:
            positions.append(pos)
            start = pos + 1
        else:
            break
    return positions