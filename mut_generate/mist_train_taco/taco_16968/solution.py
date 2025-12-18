"""
QUESTION:
Its NU-Tech'15 and participants are pouring in large numbers. Its the first day of the fest and everybody has gathered around the registration desks but are confused on receiving a set of very large numbers on the registration slip. They are later told by the volunteers that in order to get their respective registration numbers, they are supposed to add all the numbers, then add the digits of the sum and the then again add the digits of the new sum and continue till the answer consists of a single digit. That digit is their Registration ID. Help the participants to decipher their NU-Tech Ids.

Input:

First line contains an integer n. n lines follow each containing a "Large Number".

Output:

Print the Registration IDs of the student.

Constraints:

1 ≤ n ≤500

1 ≤ Large Number ≤ 2^1000

SAMPLE INPUT
2
23
99

SAMPLE OUTPUT
5
"""

def calculate_registration_id(numbers):
    # Step 1: Sum all the numbers
    total_sum = sum(int(num) for num in numbers)
    
    # Step 2: Reduce the sum to a single digit
    while total_sum >= 10:
        temp_sum = 0
        while total_sum > 0:
            temp_sum += total_sum % 10
            total_sum //= 10
        total_sum = temp_sum
    
    return total_sum