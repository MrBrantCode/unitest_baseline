"""
QUESTION:
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need.

### Example:
```python
paperwork(5, 5) == 25
```

**Note:** if `n < 0` or `m < 0` return `0`!

Waiting for translations and Feedback! Thanks!
"""

def calculate_total_pages(n: int, m: int) -> int:
    """
    Calculate the total number of pages needed for paperwork.

    Parameters:
    n (int): Number of classmates.
    m (int): Number of pages per classmate.

    Returns:
    int: Total number of pages needed. Returns 0 if either n or m is less than 0.
    """
    return n * m if n > 0 and m > 0 else 0