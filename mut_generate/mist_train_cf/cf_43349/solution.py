"""
QUESTION:
Write a function `calculate_sums_and_parity` that takes a list of integers as input and returns a tuple containing a list of sums of the digits in each integer and a list of tuples, where each tuple contains the sum of even digits and the sum of odd digits in the corresponding integer. 

The input list should contain exactly three integers, each with six digits. 

Do not use built-in sort functions.
"""

def calculate_sums_and_parity(input_nums):
    """
    Calculate the sum of digits in each integer and the sum of even and odd digits.

    Args:
    input_nums (list): A list of three integers, each with six digits.

    Returns:
    tuple: A tuple containing a list of sums of the digits in each integer and a list of tuples, 
           where each tuple contains the sum of even digits and the sum of odd digits in the corresponding integer.
    """
    sums = []
    parity = []
    for num in input_nums:
        str_num = str(num)
        sum_num = 0
        even = 0
        odd = 0
        for ch in str_num:
            n = int(ch)
            sum_num += n
            if n % 2 == 0:
                even += n
            else:
                odd += n
        sums.append(sum_num)
        parity.append((even, odd))
    return sums, parity