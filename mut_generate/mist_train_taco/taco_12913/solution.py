"""
QUESTION:
Every Turkish citizen has an identity number whose validity can be checked by these set of rules:

- It is an 11 digit number
- First digit can't be zero
- Take the sum of 1st, 3rd, 5th, 7th and 9th digit and multiply it by 7.
Then subtract the sum of 2nd, 4th, 6th and 8th digits from this value.
Modulus 10 of the result should be equal to 10th digit.
- Sum of first ten digits' modulus 10 should be equal to eleventh digit.

Example:

    10167994524
    //  1+1+7+9+5= 23   // "Take the sum of 1st, 3rd, 5th, 7th and 9th digit..."
    //    23 * 7= 161   //  "...and multiply it by 7"
    //   0+6+9+4 = 19   // "Take the sum of 2nd, 4th, 6th and 8th digits..."
    // 161 - 19 = 142   // "...and subtract from first value"
    // "Modulus 10 of the result should be equal to 10th digit"
    10167994524
             ^ = 2 = 142 % 10
    // 1+0+1+6+7+9+9+4+5+2 = 44
    // "Sum of first ten digits' modulus 10 should be equal to eleventh digit"
    10167994524
              ^ = 4 = 44 % 10

Your task is to write a function to check the validity of a given number.
Return `true` or `false` accordingly.

Note: The input can be a string in some cases.
"""

def is_valid_tr_identity_number(tr_number):
    # Convert the input to a string for consistent processing
    tr_number_str = str(tr_number)
    
    # Check if the length is 11 and the first digit is not zero
    if len(tr_number_str) != 11 or tr_number_str[0] == '0':
        return False
    
    # Extract digits for calculations
    digits = list(map(int, tr_number_str))
    
    # Calculate the sum of 1st, 3rd, 5th, 7th, and 9th digits
    sum_odd_positions = sum(digits[i] for i in range(0, 10, 2))
    
    # Calculate the sum of 2nd, 4th, 6th, and 8th digits
    sum_even_positions = sum(digits[i] for i in range(1, 9, 2))
    
    # Calculate the required values for validation
    result_1 = (sum_odd_positions * 7 - sum_even_positions) % 10
    result_2 = sum(digits[:10]) % 10
    
    # Check if the results match the 10th and 11th digits respectively
    return result_1 == digits[9] and result_2 == digits[10]