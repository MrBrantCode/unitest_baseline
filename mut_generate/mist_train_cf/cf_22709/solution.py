"""
QUESTION:
Write a function `powers_of_two(n)` that prints all powers of 2 less than or equal to `n` along with their binary representations and the sum of their binary digits. The function should also return or print the total sum of all binary digits. The function should take an integer `n` as input.
"""

def powers_of_two(n):
    total_sum = 0

    for i in range(n):
        if 2 ** i <= n:
            binary_rep = bin(2 ** i)[2:]
            binary_sum = sum(int(digit) for digit in binary_rep)
            total_sum += binary_sum

            print(f"{2 ** i}: {binary_rep} ({'+'.join(list(binary_rep))} = {binary_sum})")

    print(f"Total sum of binary digits: {total_sum}")
    return total_sum