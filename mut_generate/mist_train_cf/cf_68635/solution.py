"""
QUESTION:
Create a function `anagram_checker` that takes two string parameters and an optional error rate parameter, and returns a boolean value. The function should determine if two strings are anagrams despite minor errors (substitutions or differences in 2-3% of the total string length), ignore leading/trailing spaces, underscores, and hyphens, and consider the comparison case-insensitive. The error rate parameter should default to 0.02 if not provided.
"""

def anagram_checker(str1: str, str2: str, error_rate: float = 0.02) -> bool:
    str1 = str1.replace(' ', '').replace('_', '').replace('-', '').lower()
    str2 = str2.replace(' ', '').replace('_', '').replace('-', '').lower()

    # Calculate the target length based on error_rate
    target_length = (1 - error_rate) * len(str1)

    str1_counter = Counter(str1)
    str2_counter = Counter(str2)

    common = str1_counter & str2_counter
    common_count = sum(common.values())
    
    # More than `error_rate` % of the characters are the same
    return common_count >= target_length