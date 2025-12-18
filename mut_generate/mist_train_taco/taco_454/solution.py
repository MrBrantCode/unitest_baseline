"""
QUESTION:
-----Input-----

The input contains a single integer $a$ ($1 \le a \le 99$).


-----Output-----

Output "YES" or "NO".


-----Examples-----
Input
5

Output
YES

Input
13

Output
NO

Input
24

Output
NO

Input
46

Output
YES
"""

def check_number_contains_letters(a: int) -> str:
    k = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    n = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if a < 20:
        a_str = k[a]
    else:
        a_str = n[a // 10] + k[a % 10]
    
    if 'k' in a_str or 'a' in a_str or 'n' in a_str:
        return 'NO'
    else:
        return 'YES'