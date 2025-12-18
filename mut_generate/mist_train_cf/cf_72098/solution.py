"""
QUESTION:
Create a function `analyze_sequence` that takes a string `text` and a subsequence `q` as input, and returns a tuple containing the first appearing position, the count, and the last appearing position of `q` in `text`. The function should have an optional parameter `ignore_case` (default is `False`) that, if set to `True`, makes the search case-insensitive by converting both `text` and `q` to lowercase. The function should return `-1` for the first and last position and `0` for the count if `q` is not found in `text`.
"""

def analyze_sequence(text, q, ignore_case=False):
    if ignore_case:
        text = text.lower()
        q = q.lower()

    first_appearance = text.find(q)
    if first_appearance == -1:
        return (first_appearance, 0, -1)

    last_appearance = text.rfind(q)
    count = text.count(q)

    return (first_appearance, count, last_appearance)