"""
QUESTION:
Create a function `custom_mix_strings(s1, s2)` that merges two input strings `s1` and `s2` by alternating their characters. The function should handle cases where `s1` and `s2` have different lengths. The merged string should be ordered by ASCII values in descending order, and then returned in reverse order.
"""

def custom_mix_strings(s1: str, s2: str) -> str:
    """Mix two strings by alternating their characters, ordering them by ASCII values and reversing the final string."""
    
    result = []
    
    min_length = min(len(s1), len(s2))
    
    for i in range(min_length):
        result.append(s1[i])
        result.append(s2[i])
        
    if len(s1) > len(s2):
        result.extend(list(s1[min_length:]))
    else:
        result.extend(list(s2[min_length:]))

    result.sort(key=ord, reverse=True)

    final_string = ''.join(result)
    
    return final_string