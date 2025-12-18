"""
QUESTION:
Write a function called "concatenate_elements" that receives four parameters: a list of strings `words`, a string `separator`, and two boolean parameters `odd_positions_only` and `consecutive_primes` (both defaulting to False). The function should combine all the elements in the list `words` with the string `separator`. If `odd_positions_only` is True, the `separator` should be used only between elements with odd index positions. If `consecutive_primes` is True, the `separator` should only be inserted between elements that are at prime index positions.
"""

from typing import List

# helper function to check if a number is prime
def is_prime(n: int) -> bool:
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))
  
def concatenate_elements(words: List[str], separator: str, odd_positions_only: bool = False, consecutive_primes: bool = False) -> str:
    res = [separator.join([words[i] for i in range(len(words)) if (odd_positions_only and i % 2 != 0) or (consecutive_primes and is_prime(i)) or (not odd_positions_only and not consecutive_primes)])]
    return separator.join(res)