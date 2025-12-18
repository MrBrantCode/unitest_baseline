"""
QUESTION:
Same as [the original](https://www.codewars.com/kata/simple-fun-number-258-is-divisible-by-6) (same rules, really, go there for example and I strongly recommend completing it first), but with more than one asterisk (but always at least one).

For example, `"*2"` should return `["12", "42", "72"]`.

Similarly, `"*2*"` should return `["024", "120", "126", "222", "228", "324", "420", "426", "522", "528", "624", "720", "726", "822", "828", "924"]`. Order matters and returning the right one is part of the challenge itself, yep!

More examples in the test codes and, of course, if you cannot generate any number divisible by 6, just return `[]` (or `[] of String` in Crystal).
"""

from itertools import product

def find_divisible_by_6_combinations(s: str) -> list[str]:
    # If the last character is odd, no number can be divisible by 6
    if s[-1] in '13579':
        return []
    
    # Replace '*' with '{}' for formatting
    ss = s.replace('*', '{}')
    
    # Generate all possible combinations of digits to replace '*'
    combinations = [ss.format(*p) for p in product(*['0123456789'] * s.count('*'))]
    
    # Filter combinations to find those divisible by 6
    return [v for v in combinations if int(v) % 6 == 0]