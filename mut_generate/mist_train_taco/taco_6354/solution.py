"""
QUESTION:
Luke Skywalker gave Chewbacca an integer number x. Chewbacca isn't good at numbers but he loves inverting digits in them. Inverting digit t means replacing it with digit 9 - t. 

Help Chewbacca to transform the initial number x to the minimum possible positive number by inverting some (possibly, zero) digits. The decimal representation of the final number shouldn't start with a zero.


-----Input-----

The first line contains a single integer x (1 ≤ x ≤ 10^18) — the number that Luke Skywalker gave to Chewbacca.


-----Output-----

Print the minimum possible positive number that Chewbacca can obtain after inverting some digits. The number shouldn't contain leading zeroes.


-----Examples-----
Input
27

Output
22

Input
4545

Output
4444
"""

def transform_chewbacca_number(x: int) -> int:
    # Convert the number to a list of its digits
    digits = [int(d) for d in str(x)]
    
    # Iterate over each digit and apply the inversion rule
    for i, digit in enumerate(digits):
        if i == 0 and digit == 9:
            continue  # Skip the first digit if it's 9 to avoid leading zero
        if digit > 4:
            digits[i] = 9 - digit
    
    # Convert the list of digits back to an integer
    transformed_number = int(''.join(str(d) for d in digits))
    
    return transformed_number