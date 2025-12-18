"""
QUESTION:
Write a function `format_large_number(n)` that formats a given integer `n` to enhance its comprehensibility by adding commas as thousands separators. The function should handle both positive and negative integers, as well as zero. The commas should be placed properly for easier reading, taking into account potential exceptions that might arise from different integer inputs.
"""

def format_large_number(n):
    return '{:,}'.format(n)