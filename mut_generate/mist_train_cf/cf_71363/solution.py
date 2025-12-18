"""
QUESTION:
Create a function called `concatenate_elements` that takes a list of strings `words`, a string `separator`, and two optional parameters `odd_positions_only` (default False) and `consecutive_primes` (default False). The function should return a string with the elements from the `words` list concatenated with the `separator`. 

If `odd_positions_only` is True, include the `separator` only between elements with odd indices. If `consecutive_primes` is True, include the `separator` only between elements with consecutive prime indices. If neither `odd_positions_only` nor `consecutive_primes` is True, include the `separator` between all elements.
"""

from typing import List

def concatenate_elements(words: List[str], separator: str, 
                         odd_positions_only: bool = False, 
                         consecutive_primes: bool = False) -> str:
    
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    result = []
    
    if odd_positions_only:
        for i in range(len(words)):
            if i % 2 != 0:
                result.append(separator + words[i])
            else:
                result.append(words[i])
    elif consecutive_primes:
        for i in range(len(words)):
            if i != 0 and is_prime(i) and is_prime(i - 1):
                result.append(separator + words[i])
            else:
                result.append(words[i])
    else:
        return separator.join(words)
    
    return "".join(result)