"""
QUESTION:
A Sky bag to lock accepts only the Prime number (all combination of prime numbers are allowed) except ignoring the leading zero's (0's). If there is prime number like '003' or '103' both of them are considered as the valid codes to unlock the Sky bag, but these are the 3 digit numbers.

In a sky bag, the numbered are in the sequence of 0-9, and the digit '0' comes before the '1' and after the '9'. Now, in a single step you are allowed to rotate 1 digit weather next or previous.

Now, you have to calculate the minimum number of steps required to unlock the Sky bag and you will get the Current code as well as the prime lock of  N digits.

INPUT

Number of Test Cases T.

Each Test case contains an integer N, and then proceeding with the N decimal digits which represents the current code.

OUTPUT

For each Test case, print the minimum number of steps required to unlock the Sky bag.

CONSTRAINTS

T < 10^5

1 ≤ N ≤ 6

Note :- To be Eligible for Prizes you have to register and create your home address maptag.

Click here to create your Maptag

SAMPLE INPUT
3
3 001
5 45654
4 1234

SAMPLE OUTPUT
1
3
2

Explanation

Example 1 :- To get 002, you need to change 1 to 2
Example 2 :- To get 35753, you need to change 4 to 3, 6 to 7 and 4 to 3.
Example 3 :- To get 0233, you need to change 1 to 0 and 4 to 3.
"""

def calculate_min_steps_to_unlock(test_cases):
    def check_and_change_to_prime(n):
        if n == 9 or n == 8:
            return 7
        for p in range(n, 2 * n):
            for i in range(2, p):
                if p % i == 0:
                    break
            else:
                return p
        return None

    results = []
    
    for case in test_cases:
        N, current_code = case
        count = 0
        for digit in current_code:
            digit = int(digit)
            if digit != 0:
                if digit == 1:
                    count += 1
                else:
                    count += abs(digit - check_and_change_to_prime(digit))
        results.append(count)
    
    return results