"""
QUESTION:
In Byteland,conversion of numbers between different bases has  always been a herculian task.They always make errors in these conversions.
People in Byteland  always write one of the digits wrong when they convert a number to a new base and write it down.  For example, when they convert
the number 56 into binary (base 2), the correct result should be
"110", but they might instead write down "010" or "111".  They never
accidentally delete or add digits, so they might write down a number with
a leading digit of "0" if this is the digit they get wrong.

You are given Bytelandians' output when converting a number N into base 2 and base 3,
Find out the correct original value of N (in base 10). You can
assume that there is a unique solution for N.

Input
There are 2 lines:
Line 1: The base-2 representation of N, with one digit written
        incorrectly.
Line 2: The base-3 representation of N, with one digit written
        incorrectly.

Output
The correct value of N

Constraints
N ≤ 1 billion

SAMPLE INPUT
1010
212

SAMPLE OUTPUT
14
"""

def find_correct_number(base2_str: str, base3_str: str) -> int:
    def base3_modifier(base3_list: list, iteration: int) -> int:
        local_base3 = list(base3_list)
        bit_loc = int(iteration / 2)
        bit_remainder = iteration % 2
        if bit_remainder == 0:
            if local_base3[bit_loc] == '2':
                local_base3[bit_loc] = '1'
            elif local_base3[bit_loc] == '1':
                local_base3[bit_loc] = '0'
            else:
                local_base3[bit_loc] = '2'
        else:
            if local_base3[bit_loc] == '2':
                local_base3[bit_loc] = '0'
            elif local_base3[bit_loc] == '1':
                local_base3[bit_loc] = '2'
            else:
                local_base3[bit_loc] = '1'
        return int(''.join(local_base3), 3)

    base2 = int(base2_str, 2)
    base2_range = len(base2_str)
    base3_range = 2 * len(base3_str)

    for i in range(base2_range):
        mod_base2 = base2 ^ (1 << i)
        for j in range(base3_range):
            mod_base3 = base3_modifier(base3_str, j)
            if mod_base2 == mod_base3:
                return mod_base2

    # If no match is found, return -1 (though the problem guarantees a unique solution)
    return -1