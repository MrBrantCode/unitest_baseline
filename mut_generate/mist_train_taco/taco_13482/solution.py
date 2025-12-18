"""
QUESTION:
One cold winter evening Alice and her older brother Bob was sitting at home near the fireplace and giving each other interesting problems to solve. When it was Alice's turn, she told the number n to Bob and said:

—Shuffle the digits in this number in order to obtain the smallest possible number without leading zeroes.

—No problem! — said Bob and immediately gave her an answer.

Alice said a random number, so she doesn't know whether Bob's answer is correct. Help her to find this out, because impatient brother is waiting for the verdict.

Input

The first line contains one integer n (0 ≤ n ≤ 109) without leading zeroes. The second lines contains one integer m (0 ≤ m ≤ 109) — Bob's answer, possibly with leading zeroes.

Output

Print OK if Bob's answer is correct and WRONG_ANSWER otherwise.

Examples

Input

3310
1033


Output

OK


Input

4
5


Output

WRONG_ANSWER
"""

def check_bob_answer(n, m):
    # Convert the original number to a string and sort its digits
    sorted_digits = sorted(str(n))
    
    # Count the number of zeros
    zero_count = sorted_digits.count('0')
    
    # Construct the smallest possible number without leading zeros
    smallest_number = ''
    if len(sorted_digits) > zero_count:
        smallest_number += sorted_digits[zero_count]
    for i in range(zero_count):
        smallest_number += sorted_digits[i]
    for i in range(zero_count + 1, len(sorted_digits)):
        smallest_number += sorted_digits[i]
    
    # Compare Bob's answer with the smallest possible number
    if str(m) == smallest_number:
        return 'OK'
    else:
        return 'WRONG_ANSWER'