"""
QUESTION:
Write a Python function `resumo` that takes three parameters: `n` (initial value), `aumento` (list of percentage increases), and `reducao` (list of percentage decreases). The function should apply the percentage increases and decreases to the initial value in the given order, display each step with a message, and return the final calculated value.
"""

def resumo(n, aumento, reducao):
    valor = n
    print(f'Initial value:                 {valor:>10}')
    for a in aumento:
        valor *= (1 + a/100)
        print(f'Increase by {a}%:             {valor:>.2f}')
    for r in reducao:
        valor *= (1 - r/100)
        print(f'Decrease by {r}%:             {valor:>.2f}')
    return valor