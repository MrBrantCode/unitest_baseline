"""
QUESTION:
Create a function called `format_range` that takes in two integer arguments: `start` and `end`. The function should return a list of strings, where each string represents a number in the range from `start` to `end` (inclusive), formatted with commas as thousand separators. The range should be inclusive, meaning it should include both the `start` and `end` values. The function should work for both ascending and descending ranges, and it should handle negative numbers correctly.

Constraints:
- The input numbers `start` and `end` are integers within the range [-10^6, 10^6].
- If `start` is larger than `end`, the function should count down.
- If `start` and `end` are the same, the function should output that number correctly formatted.
- If `start` is smaller, the function should count up to `end`.
"""

def format_range(start, end):
    step = -1 if start > end else 1
    return [f'{i:,}' for i in range(start, end+step, step)]