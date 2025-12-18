"""
QUESTION:
Write a function `generate_permutations` that generates all permutations of a given string, including duplicates, while maintaining the order of appearance. The string can contain 1 to 8 alphanumeric characters, including letters, numbers, or special characters, and is case-sensitive.

The function should have the following signature:
```python
def generate_permutations(s: str) -> List[str]
```
"""

from typing import List

def generate_permutations(s: str) -> List[str]:
    if len(s) == 1:
        return [s]

    def occurrences(arr: List[str]) -> dict[str, int]:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        return freq

    occ = occurrences(list(s))
    perms = []
    for char, count in occ.items():
        if count > 0:
            occ[char] = count - 1
            for perm in generate_permutations("".join(char * cnt for char, cnt in occ.items())):
                perms.append(char + perm)
            occ[char] = count
    return perms