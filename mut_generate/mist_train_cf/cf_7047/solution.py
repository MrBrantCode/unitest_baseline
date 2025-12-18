"""
QUESTION:
Write a function `is_consecutive_primes` that checks if a given string of numbers represents a sequence of 4 consecutive prime numbers, where each prime number is followed by a non-prime number.
"""

import re

def is_consecutive_primes(s):
    """
    Checks if a given string of numbers represents a sequence of 4 consecutive prime numbers, 
    where each prime number is followed by a non-prime number.

    Args:
    s (str): The input string of numbers.

    Returns:
    bool: True if the string represents a sequence of 4 consecutive prime numbers followed by a non-prime number, False otherwise.
    """
    pattern = r"^(2|3|5|7)(11|13|17|19)(23|29|31|37)(41|43|47|53)(4|6|8|9|10|12|14|15|16|18|20|21|22|24|25|26|27|28|30|32|33|34|35|36|38|39|40|42|44|45|46|48|49|50|51|52|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100)$"
    return bool(re.match(pattern, s))