"""
QUESTION:
Write a function `fib_to_septenary(n)` that generates a septenary (base 7) digit sequence fulfilling the Fibonacci series logic until the sequence length reaches `n` characters. The sequence should not exceed `n` characters.
"""

def fib_to_septenary(n):
    def convert_to_septenary(num):
        sev_num = ''
        if num == 0:
            return '0'
        else:
            while num > 0:
                sev_num = str(num % 7) + sev_num
                num = num // 7
        return sev_num

    fib_series = [0, 1]
    sev_series = ['0', '1']

    while len("".join(sev_series)) < n:
        next_num = fib_series[-2] + fib_series[-1]
        fib_series.append(next_num)
        next_num_sev = convert_to_septenary(next_num)
        sev_series.append(next_num_sev)
    sequence = "".join(sev_series)

    if len(sequence) > n:
        sequence = sequence[:n]
    return sequence