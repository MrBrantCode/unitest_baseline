"""
QUESTION:
Step through my `green glass door`.

You can take the `moon`, but not the `sun`.

You can take your `slippers`, but not your `sandals`.

You can go through `yelling`, but not `shouting`.

You can't run through `fast`, but you can run with `speed`.

You can take a `sheet`, but not your `blanket`.

You can wear your `glasses`, but not your `contacts`.

Have you figured it out? Good! Then write a program that can figure it out as well.
"""

def can_step_through(word: str) -> bool:
    """
    Determines if a given word can step through the green glass door.

    The green glass door allows words that have two consecutive identical letters.

    Args:
        word (str): The word to be checked.

    Returns:
        bool: True if the word can step through the green glass door, False otherwise.
    """
    return any((m == n for (m, n) in zip(word, word[1:])))