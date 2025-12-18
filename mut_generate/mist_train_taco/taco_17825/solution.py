"""
QUESTION:
Check your arrows
You have a quiver of arrows, but some have been damaged. The quiver contains arrows with an optional range information (different types of targets are positioned at different ranges), so each item is an arrow.

You need to verify that you have some good ones left, in order to prepare for battle:
```python
anyArrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])
```

If an arrow in the quiver does not have a damaged status, it means it's new.

The expected result is a boolean, indicating whether you have any good arrows left.

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
"""

def has_good_arrows(arrows):
    """
    Check if there are any good (not damaged) arrows in the quiver.

    Parameters:
    arrows (list of dict): A list of dictionaries representing arrows. Each dictionary may contain keys such as 'range' and 'damaged'.

    Returns:
    bool: True if there is at least one arrow that is not damaged, False otherwise.
    """
    return any(not arrow.get('damaged', False) for arrow in arrows)